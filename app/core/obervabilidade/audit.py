from functools import wraps
from app.core.obervabilidade.logger import logger


def audit(action: str):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            logger.info(
                "audit.start",
                extra={"extra_data": {"action": action}}
            )

            try:
                result = fn(*args, **kwargs)

                logger.info(
                    "audit.success",
                    extra={"extra_data": {"action": action}}
                )

                return result

            except Exception:
                logger.exception(
                    "audit.fail",
                    extra={"extra_data": {"action": action}}
                )
                raise

        return wrapper
    return decorator
