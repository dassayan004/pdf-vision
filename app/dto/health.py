from pydantic import BaseModel, Field


class MemoryHealth(BaseModel):
    heap_used_mb: float = Field(..., description="Heap memory used (MB)")
    rss_used_mb: float = Field(..., description="Resident Set Size (MB)")
    status: str = Field(..., description="Memory health status")


class DiskHealth(BaseModel):
    total_gb: float = Field(..., description="Total disk space (GB)")
    used_gb: float = Field(..., description="Used disk space (GB)")
    free_gb: float = Field(..., description="Free disk space (GB)")
    percent_used: float = Field(..., description="Disk usage percent")
    status: str = Field(..., description="Disk health status")


class HealthCheckResponse(BaseModel):
    status: str = Field(..., description="Overall system health")
    memory: MemoryHealth
    disk: DiskHealth
