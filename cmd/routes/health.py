from fastapi import APIRouter

from cmd import deps

router = APIRouter(tags=["Health"])

@router.get("/health")
async def health():
    return {
        "status": "ok" if deps.app_ready else "starting",
        "service": "IntelligentAssistant",
    }
