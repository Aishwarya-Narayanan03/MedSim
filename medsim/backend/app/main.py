from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import login, embed, llm, cases, admin
from app.utils.secrets import load_secrets
import os

app = FastAPI(title="MedSim Backend", version="1.0.0")

# Load secrets at startup
env_secrets = load_secrets()

origins = env_secrets.get('FRONTEND_ALLOWED_DOMAINS', '*').split(',')
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router, prefix="/login", tags=["login"])
app.include_router(embed.router, prefix="/embed", tags=["embedding"])
app.include_router(llm.router, prefix="/llm", tags=["llm"])
app.include_router(cases.router, prefix="/cases", tags=["cases"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/")
def root():
    return {"status": "MedSim Backend running"}
