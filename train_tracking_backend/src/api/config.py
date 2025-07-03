"""
Central configuration for the backend service:
- Loads from environment variables (.env)
- Used for DB url, CORS, external APIs, etc.
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./traintracker.db")

    # CORS
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

    # External API ("Where's my train")
    WMT_API_BASE: str = os.getenv("WMT_API_BASE", "https://api.wheremytrain.com/")
    WMT_API_KEY: str = os.getenv("WMT_API_KEY", "your-api-key")

settings = Settings()
