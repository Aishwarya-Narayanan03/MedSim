import os
from jose import jwt, JWTError
from fastapi import HTTPException

OIDC_CLIENT_ID = os.getenv('OIDC_CLIENT_ID')

# For demo: use Google's public keys (in prod, cache and rotate)
GOOGLE_JWKS_URL = 'https://www.googleapis.com/oauth2/v3/certs'
import requests

_jwks = None

def get_jwks():
    global _jwks
    if _jwks is None:
        _jwks = requests.get(GOOGLE_JWKS_URL).json()
    return _jwks

def verify_jwt(token: str):
    try:
        jwks = get_jwks()
        unverified_header = jwt.get_unverified_header(token)
        key = next(k for k in jwks['keys'] if k['kid'] == unverified_header['kid'])
        payload = jwt.decode(token, key, algorithms=['RS256'], audience=OIDC_CLIENT_ID)
        return payload
    except Exception as e:
        raise HTTPException(status_code=401, detail=f"JWT verification failed: {e}")
