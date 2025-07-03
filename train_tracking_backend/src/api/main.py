"""
Main entrypoint for the FastAPI backend for Real-Time Train Tracker.

Handles:
- App initialization & OpenAPI doc metadata
- CORS middleware config
- Database connection setup via SQLAlchemy
- Loading env/config for external 'Where’s my train' API integration
- Router includes for API structure (future)

Directory Scaffolding:
- models/: Pydantic/SQLAlchemy models
- crud/: CRUD operations centralized
- services/: Business logic and external API wrappers

PUBLIC_INTERFACE
"""

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Load .env variables
load_dotenv()

# App Metadata (for OpenAPI docs)
app = FastAPI(
    title="Real-Time Train Tracker API",
    description=(
        "Backend service for the mobile app that allows users to track trains in real time. "
        "Integrates with 'Where's my train' API, handles user authentication, search, favorites, "
        "live status, and notifications."
    ),
    version="1.0.0",
)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Database Configuration ---
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./traintracker.db")
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# --- External API Config: "Where's my train" ---
WHERES_MY_TRAIN_API_BASE = os.getenv("WMT_API_BASE", "https://api.wheremytrain.com/")
WHERES_MY_TRAIN_API_KEY = os.getenv("WMT_API_KEY", "your-api-key")  # Placeholder only

# Add relevant routers from routers/ (or api endpoints), e.g.:
# from .routers import trains, auth, users, notifications
# app.include_router(trains.router)
# app.include_router(auth.router)
# etc.

# --- Health Check Endpoint ---
# PUBLIC_INTERFACE
@app.get("/", tags=["Health"])
def health_check():
    """
    Health check endpoint for deployment and monitoring.
    Returns 200 OK if the service is up.
    """
    return {"message": "Healthy"}

# --- Dependency for DB sessions ---
# PUBLIC_INTERFACE
def get_db():
    """
    Dependency for getting a SQLAlchemy session.
    Yields a db session for each request.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- Placeholder for WMT API Wrapper (service layer stub) ---
# PUBLIC_INTERFACE
def get_train_status_from_external_api(train_id: str):
    """
    Calls 'Where's my train' external API to fetch live status for a train.

    Args:
        train_id (str): The train's unique identifier (number or name).

    Returns:
        dict: Live status information of the train.
    """
    # Example: use requests or httpx to call external API (to be implemented in services/wmt_api.py)
    # This is a placeholder/stub.
    raise NotImplementedError("Integration with 'Where's my train' API not implemented yet.")

