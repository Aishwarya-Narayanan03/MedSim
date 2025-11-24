# MedSim Backend (FastAPI)

This is the backend API for MedSim, built with FastAPI and designed for GCP Cloud Run.

## Features
- Google OIDC JWT verification (Identity Platform)
- Endpoints: /login/verify, /embed, /llm/eval, /cases/upload, /cases/list, /admin/verify
- Firestore, GCS, BigQuery, Vertex AI integration
- Secrets Manager loader (local + cloud)
- JWT verification middleware
- OpenAPI docs at `/docs`

## Local Development

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.template` to `.env` and fill in your values:
   ```bash
   cp .env.template .env
   ```
3. Run locally:
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
   ```

## Deployment
- Containerized for Cloud Run
- See root README for full stack deployment
