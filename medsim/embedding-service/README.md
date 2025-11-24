# MedSim Embedding Service

FastAPI wrapper for Vertex Embeddings. Switchable between mock and real Vertex via USE_VERTEX_MOCK env var.

- Containerized for Cloud Run
- POST /embed

## Local Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```
