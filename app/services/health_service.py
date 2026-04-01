import shutil

import psutil

from app.dto.health import DiskHealth, MemoryHealth


class HealthService:
    """Service providing system health indicators."""

    @staticmethod
    def check_heap(threshold_bytes: int) -> MemoryHealth:
        """Check heap memory (virtual memory)."""
        process = psutil.Process()
        mem_info = process.memory_info()
        heap_used = mem_info.vms
        rss_used = mem_info.rss

        heap_mb = heap_used / (1024 * 1024)
        rss_mb = rss_used / (1024 * 1024)

        status = (
            "OK"
            if heap_used < threshold_bytes and rss_used < threshold_bytes
            else "WARN"
        )

        return MemoryHealth(
            heap_used_mb=heap_mb,
            rss_used_mb=rss_mb,
            status=status,
        )

    @staticmethod
    def check_disk(threshold_percent: float, path: str = "/") -> DiskHealth:
        """Check disk health."""
        disk_usage = shutil.disk_usage(path)
        total_gb = disk_usage.total / (1024 * 1024 * 1024)
        used_gb = disk_usage.used / (1024 * 1024 * 1024)
        free_gb = disk_usage.free / (1024 * 1024 * 1024)
        percent_used = (disk_usage.used / disk_usage.total) * 100

        status = "OK" if percent_used < (100 - threshold_percent) else "LOW SPACE"

        return DiskHealth(
            total_gb=total_gb,
            used_gb=used_gb,
            free_gb=free_gb,
            percent_used=percent_used,
            status=status,
        )
