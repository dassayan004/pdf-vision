from fastapi import APIRouter, status

from app.dto.health import HealthCheckResponse
from app.services.health_service import HealthService

router = APIRouter(tags=["Health"])


@router.get(
    "/health",
    summary="Perform a Health Check",
    response_description="Return HTTP Status Code 200 (OK)",
    status_code=status.HTTP_200_OK,
    response_model=HealthCheckResponse,
)
async def health_check() -> HealthCheckResponse:
    """
    Performs:
    - Memory heap check
    - Memory RSS check
    - Disk space check
    """
    memory = HealthService.check_heap(threshold_bytes=1000 * 1024 * 1024)
    disk = HealthService.check_disk(threshold_percent=10, path="/")

    overall_status = (
        "OK" if memory.status == "OK" and disk.status == "OK" else "DEGRADED"
    )

    return HealthCheckResponse(
        status=overall_status,
        memory=memory,
        disk=disk,
    )
