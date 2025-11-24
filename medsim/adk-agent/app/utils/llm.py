import os
import httpx

async def call_llm(case):
    endpoint = os.getenv('VERTEX_LLM_API')
    async with httpx.AsyncClient() as client:
        resp = await client.post(endpoint, json={"case": case})
        return resp.json().get('result')
