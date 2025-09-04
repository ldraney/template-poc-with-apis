import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = os.getenv("APP_NAME", "Namespace Service")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./data/namespace.db")
    
    # Server
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    RELOAD: bool = os.getenv("RELOAD", "False").lower() == "true"
    
    # Paths
    BASE_DIR = Path(__file__).resolve().parent.parent
    TEMPLATES_DIR = BASE_DIR / "frontend" / "templates"
    STATIC_DIR = BASE_DIR / "frontend" / "static"
    
    # External Services (to be configured per POC)
    CLIENT_SERVICE_URL: str = os.getenv("CLIENT_SERVICE_URL", "http://localhost:7012")
    PRICING_SERVICE_URL: str = os.getenv("PRICING_SERVICE_URL", "http://localhost:7013")
    FORMULA_SERVICE_URL: str = os.getenv("FORMULA_SERVICE_URL", "http://localhost:7014")
    
    # Feature Flags
    ENABLE_CLIENT_INTEGRATION: bool = os.getenv("ENABLE_CLIENT_INTEGRATION", "True").lower() == "true"
    ENABLE_PRICING_INTEGRATION: bool = os.getenv("ENABLE_PRICING_INTEGRATION", "True").lower() == "true"

settings = Settings()