from fastapi import APIRouter, Request
from app.services.firestore import verify_user

router = APIRouter()

@router.post("/verify")
def admin_verify(request: Request):
    data = request.json()
    user_id = data.get("user_id")
    verify_user(user_id)
    return {"status": "verified"}
