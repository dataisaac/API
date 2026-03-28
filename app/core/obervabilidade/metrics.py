import time
from functools import wraps
from app.core.obervabilidade.logger import logger


def timed(metric_name: str):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()

            try:
                return fn(*args, **kwargs)
            finally:
                ms = (time.perf_counter() - start) * 1000
                logger.info(
                    "metric",
                    extra={
                        "extra_data": {
                            "metric": metric_name,
                            "duration_ms": round(ms, 2)
                        }
                    }
                )

        return wrapper
    return decorator
