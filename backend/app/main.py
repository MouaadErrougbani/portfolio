from fastapi import FastAPI
from app.config import settings
from sqlalchemy import text
from app.db.engine import engine

from contextlib import asynccontextmanager


app = FastAPI(
    title=settings.APP_NAME,
)


@app.get("/")
def root():
    return {
        "message": "Portfolio Backend Running 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/db-test")
def db_test():
    with engine.connect() as connection:
        version = connection.execute(
            text("SELECT version();")
        ).scalar()

    return {
        "database": "connected",
        "version": version,
    }


