import os
import httpx

async def get_embedding(text):
    endpoint = os.getenv('EMBEDDINGS_SERVICE_URL')
    async with httpx.AsyncClient() as client:
        resp = await client.post(endpoint, json={"text": text})
        return resp.json().get('embedding')
