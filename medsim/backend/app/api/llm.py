from fastapi import APIRouter, Request
from app.services.vertex import run_llm_eval

router = APIRouter()

@router.post("/eval")
def llm_eval(request: Request):
    data = request.json()
    case = data.get("case")
    result = run_llm_eval(case)
    return {"result": result}
