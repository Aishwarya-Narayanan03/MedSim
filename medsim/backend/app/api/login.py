from fastapi import APIRouter, Request, HTTPException
from app.utils.jwt import verify_jwt

router = APIRouter()

@router.post("/verify")
def verify_login(request: Request):
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    payload = verify_jwt(token)
    return {"verified": bool(payload)}
