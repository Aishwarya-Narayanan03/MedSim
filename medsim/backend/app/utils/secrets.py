import os
from google.cloud import secretmanager

def load_secrets():
    secrets = {}
    # Prefer env vars for local dev
    for k in [
        'VERTEX_EMBED_API', 'VERTEX_LLM_API', 'OIDC_CLIENT_ID', 'GCS_BUCKET',
        'BQ_EVENTS_TABLE', 'FIRESTORE_COLLECTION', 'BACKEND_JWT_SECRET',
        'FRONTEND_ALLOWED_DOMAINS', 'AGENT_SYSTEM_PROMPT', 'EMBEDDINGS_SERVICE_URL', 'BACKEND_URL', 'USE_VERTEX_MOCK']:
        v = os.getenv(k)
        if v:
            secrets[k] = v
    # In cloud, load from Secret Manager if not set
    if os.getenv('K_SERVICE'):
        client = secretmanager.SecretManagerServiceClient()
        project_id = os.getenv('GOOGLE_CLOUD_PROJECT')
        for k in secrets:
            if not secrets[k]:
                name = f"projects/{project_id}/secrets/{k}/versions/latest"
                response = client.access_secret_version(request={"name": name})
                secrets[k] = response.payload.data.decode('UTF-8')
    return secrets
