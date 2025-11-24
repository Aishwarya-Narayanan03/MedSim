from fastapi import FastAPI, Request
import os
import httpx

app = FastAPI(title="MedSim Embedding Service", version="1.0.0")

@app.post("/embed")
async def embed(request: Request):
    data = await request.json()
    text = data.get("text")
    if os.getenv('USE_VERTEX_MOCK', 'true').lower() == 'true':
        return {"embedding": [0.0] * 768}
    endpoint = os.getenv('VERTEX_EMBED_API')
    async with httpx.AsyncClient() as client:
        resp = await client.post(endpoint, json={"content": text})
        return {"embedding": resp.json().get('embedding')}

@app.get("/")
def root():
    return {"status": "Embedding Service running"}
