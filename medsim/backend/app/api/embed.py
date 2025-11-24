from fastapi import APIRouter, Request
from app.utils.embeddings import get_embedding

router = APIRouter()


@router.post("")
async def embed(request: Request):
    data = await request.json()
    text = data.get("text")
    embedding = await get_embedding(text)
    return {"embedding": embedding}
