from fastapi import FastAPI, Request
from app.reasoning import chain_of_thought
from app.utils.firestore import store_memory
from app.utils.llm import call_llm
from app.utils.embeddings import get_embedding
import os

app = FastAPI(title="MedSim ADK Agent", version="1.0.0")

@app.post("/reason")
async def reason(request: Request):
    data = await request.json()
    case = data.get("case")
    memory = await store_memory(case)
    embedding = await get_embedding(case)
    result = await chain_of_thought(case, embedding, memory)
    return {"result": result}

@app.get("/")
def root():
    return {"status": "ADK Agent running"}
