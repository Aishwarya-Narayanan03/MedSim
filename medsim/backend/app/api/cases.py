from fastapi import APIRouter, UploadFile, File, Request
from app.services.gcs import upload_case_file
from app.services.firestore import list_cases

router = APIRouter()

@router.post("/upload")
def upload_case(file: UploadFile = File(...)):
    url = upload_case_file(file)
    return {"url": url}

@router.get("/list")
def get_cases():
    return list_cases()
