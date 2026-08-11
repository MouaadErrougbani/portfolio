from fastapi import FastAPI

from app.routers import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Portfolio API",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://portfolio-frontend:5173",
        "http://portfolio-frontend:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(category_router)
app.include_router(skill_router)
app.include_router(contact_router)
app.include_router(diploma_router)
app.include_router(domain_router)
app.include_router(framework_router)
app.include_router(info_router)
app.include_router(keyword_router)
app.include_router(language_router)
app.include_router(navigation_router)
app.include_router(programming_language_router)
app.include_router(project_router)
app.include_router(subdomain_router)
app.include_router(tag_router)
app.include_router(traduction_router)