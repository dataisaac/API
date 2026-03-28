import time
import uuid
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.obervabilidade.logger import logger, request_id_ctx


class ObservabilityMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, request, call_next):
        rid = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        request_id_ctx.set(rid)

        start = time.perf_counter()

        logger.info(
            "request.start",
            extra={
                "extra_data": {
                    "method": request.method,
                    "path": request.url.path,
                    "query": str(request.query_params)
                }
            }
        )

        try:
            response = await call_next(request)

        except Exception:
            logger.exception("request.error")
            raise

        duration_ms = round((time.perf_counter() - start) * 1000, 2)

        logger.info(
            "request.end",
            extra={
                "extra_data": {
                    "status": response.status_code,
                    "duration_ms": duration_ms
                }
            }
        )

        response.headers["X-Request-ID"] = rid
        return response
