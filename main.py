# Entrée FastAPI
from fastapi import FastAPI
from config import settings
from routes import client_routes, site_routes
from fastapi.middleware.cors import CORSMiddleware
from database import init_db

app = FastAPI(title="Clients Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}

app.include_router(client_routes.router)
app.include_router(site_routes.router)

# ... Autres endpoints globaux ...
