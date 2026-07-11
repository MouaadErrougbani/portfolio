# Portfolio Platform

Portfolio personnel développé avec une architecture moderne.

## Architecture

```
Internet
     │
     ▼
https://mouaad-erg.duckdns.org
     │
     ▼
Nginx (Reverse Proxy)
     │
     ├──────────────► /portfolio/
     │                     │
     │                     ▼
     │              Frontend (React + Vite)
     │                     │
     │                     ▼
     │             Appels HTTP /portfolio/api/
     │
     └──────────────► /portfolio/api/
                           │
                           ▼
                  Backend (FastAPI)
                           │
                ┌──────────┴──────────┐
                ▼                     ▼
           PostgreSQL              Redis
```

---

# Technologies

## Frontend

- React 19
- TypeScript
- Vite
- Nginx (production)

---

## Backend

- FastAPI
- SQLAlchemy
- Alembic
- Pydantic Settings

---

## Database

- PostgreSQL 17

---

## Cache

- Redis

---

## Infrastructure

- Docker
- Docker Compose
- Nginx Reverse Proxy
- Oracle Cloud Free VM

---

# Structure du projet

```
/opt

├── portfolio
│   ├── frontend
│   ├── backend
│   ├── admin
│   └── nginx
│
└── portfolio-infra
    ├── compose
    ├── database
    ├── nginx
    └── scripts
```

---

# Frontend

```
portfolio/frontend
```

Contient l'application React.

```
src/
components/
pages/
services/
hooks/
assets/
```

Compilation :

```
npm run build
```

Le résultat est placé dans

```
dist/
```

---

# Backend

```
portfolio/backend
```

Structure

```
app/

api/
core/
db/
models/
repositories/
routers/
schemas/
services/
utils/
```

Le backend est développé avec FastAPI.

---

# Base de données

Le backend communique avec PostgreSQL via SQLAlchemy.

```
FastAPI

↓

SQLAlchemy

↓

PostgreSQL
```

Les paramètres sont stockés dans

```
.env
```

Exemple

```
POSTGRES_HOST=portfolio-postgres
POSTGRES_DB=portfolio_db
POSTGRES_USER=portfolio_user
POSTGRES_PASSWORD=********
```

---

# Migrations

Les migrations sont gérées avec Alembic.

Création d'une migration

```
uv run alembic revision --autogenerate -m "message"
```

Application

```
uv run alembic upgrade head
```

Historique

```
backend/alembic/versions/
```

---

# Docker

Tous les services tournent dans Docker.

```
Frontend
Backend
PostgreSQL
Redis
PgAdmin
```

Vérifier

```
docker ps
```

Lancer

```
docker compose up -d
```

Reconstruire

```
docker compose build
```

---

# Nginx

Le serveur Nginx installé sur Ubuntu est le point d'entrée.

```
Internet

↓

Nginx

↓

Frontend
Backend
```

Configuration actuelle

```
/portfolio/
```

redirige vers

```
localhost:3000
```

et

```
/portfolio/api/
```

redirige vers

```
localhost:8000
```

---

# URLs

Frontend

```
https://mouaad-erg.duckdns.org/portfolio/
```

API

```
https://mouaad-erg.duckdns.org/portfolio/api/
```

Health

```
https://mouaad-erg.duckdns.org/portfolio/api/health
```

Database Test

```
https://mouaad-erg.duckdns.org/portfolio/api/db-test
```

---

# Cycle complet d'une requête

Lorsque l'utilisateur ouvre

```
https://mouaad-erg.duckdns.org/portfolio/
```

le parcours est :

```
Navigateur

↓

Nginx Ubuntu

↓

Container Frontend

↓

React
```

Si React appelle l'API

```
fetch("/portfolio/api/profile")
```

alors

```
React

↓

Nginx

↓

Container Backend

↓

FastAPI

↓

SQLAlchemy

↓

PostgreSQL

↓

FastAPI

↓

React

↓

Navigateur
```

---

# Services Docker

```
portfolio-frontend
```

Application React.

---

```
portfolio-backend
```

API FastAPI.

---

```
portfolio-postgres
```

Base de données PostgreSQL.

---

```
portfolio-redis
```

Cache Redis.

---

```
portfolio-pgadmin
```

Administration PostgreSQL.

---

# Développement

Frontend

```
npm install

npm run dev
```

Backend

```
uv sync

uv run uvicorn app.main:app --reload
```

---

# Production

Les conteneurs sont lancés avec Docker Compose.

Nginx expose uniquement :

```
https://mouaad-erg.duckdns.org/portfolio/
```

et

```
https://mouaad-erg.duckdns.org/portfolio/api/
```

Les ports internes (3000, 8000, 5432, 6379...) restent destinés à la communication entre les services.

---

# Objectif du projet

Construire progressivement une plateforme de portfolio moderne permettant de présenter :

- Profil
- Compétences
- Expériences
- Projets
- Blog
- Contact
- Dashboard d'administration