# MedSim

MedSim is a medical simulation learning platform built for GCP, featuring Google OIDC login, React frontend, FastAPI backend, ADK agent, Vertex AI, Firestore, BigQuery, Cloud Storage, and full CI/CD with Terraform infrastructure.

## Folder Structure
- `frontend/` - React app (Google OIDC, dashboard, uploads, semantic search)
- `backend/` - FastAPI API (OIDC, Firestore, GCS, BQ, Vertex AI)
- `adk-agent/` - Python agent for medical reasoning
- `embedding-service/` - FastAPI wrapper for Vertex Embeddings
- `mcp-toolbox/` - Python wrapper for Firestore/GCS/BQ
- `jobs/` - Cloud Tasks worker
- `infra/` - Terraform for GCP infra
- `cloudbuild.yaml` - CI/CD pipeline
- Dockerfiles for each service
- `.env` templates for all services

## Quick Start
See below for deployment, local dev, and API docs. Each service is containerized and deployable to Cloud Run. Terraform scripts provision all GCP resources. Secrets are managed via GCP Secrets Manager.

---

## Services Overview
- **Frontend:** React, Google OIDC, Firebase, role-based routing
- **Backend:** FastAPI, Firestore, GCS, BigQuery, Vertex AI, JWT
- **ADK Agent:** Python, chain-of-thought reasoning, FastAPI
- **Embedding Service:** FastAPI, Vertex Embeddings, mock/real switch
- **MCP Toolbox:** Python, Firestore/GCS/BQ wrappers
- **Jobs:** Cloud Tasks worker
- **Infra:** Terraform modules for GCP

---

## Deployment Steps
1. Configure GCP project and enable required APIs
2. Run Terraform scripts in `infra/`
3. Build and deploy containers via `cloudbuild.yaml`
4. Set up secrets in GCP Secrets Manager
5. Access frontend via Cloud Run URL

---

## API Documentation
OpenAPI docs are available for all FastAPI services. See `/docs` endpoint after deployment.

---

## Local Development
- Each service can be run locally with Docker Compose or individually
- Use `.env.local` templates for environment variables
- See service-specific README sections for details


---

For full details, see each service folder and the infra/ directory.