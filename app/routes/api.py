from fastapi import APIRouter, HTTPException
from app.config import settings

router = APIRouter()

@router.get("/status")
async def get_service_status():
    """Get service status and configuration"""
    return {
        "service": settings.APP_NAME,
        "status": "running",
        "integrations": {
            "client_service": settings.ENABLE_CLIENT_INTEGRATION,
            "pricing_service": settings.ENABLE_PRICING_INTEGRATION,
        },
        "endpoints": {
            "client_service": settings.CLIENT_SERVICE_URL,
            "pricing_service": settings.PRICING_SERVICE_URL,
            "formula_service": settings.FORMULA_SERVICE_URL,
        }
    }