# MedSim Frontend

This is the React frontend for MedSim, a medical simulation learning platform.

## Features
- Google OIDC Login (Identity Platform)
- Firebase Client integration
- Modern, animated Google OAuth login UI
- Dashboard: upload case, run LLM evaluation, semantic search, view history
- Role-based routing (verified/unverified)
- Environment variable support (VITE_...)

## Getting Started

### 1. Install dependencies
```bash
npm install
```

### 2. Configure environment variables
Copy `.env.template` to `.env` and fill in your values:
```bash
cp .env.template .env
```

### 3. Run locally
```bash
npm run dev
```

### 4. Build for production
```bash
npm run build
```

### 5. Docker build
```bash
docker build -t medsim-frontend .
```

## Folder Structure
- `src/pages` - Main pages (App, Login, Dashboard, Admin)
- `src/components` - UI components
- `src/context` - Auth context
- `src/styles` - Global styles
- `public/` - Static assets

## Deployment
This app is designed for Cloud Run deployment. See root README for full stack deployment steps.
