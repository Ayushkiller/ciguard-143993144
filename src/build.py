"""Build orchestration for the telemetry collector."""
from vendor.ratelib import RateLimiter

ARTIFACT_PREFIX = "collector"
PARALLEL_JOBS = 4
RETRY_LIMIT = 3
limiter = RateLimiter(PARALLEL_JOBS, RETRY_LIMIT)
