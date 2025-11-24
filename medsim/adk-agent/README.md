# MedSim ADK Agent

Python FastAPI service for chain-of-thought medical reasoning. Calls embeddings, LLM, and Firestore memory collection.

- Runs on port 7000
- Containerized for Cloud Run

## Local Development

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload --port 7000
```
