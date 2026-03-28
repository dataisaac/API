import logging
import json
import sys
import traceback
from datetime import datetime
from contextvars import ContextVar

sys.stdout.reconfigure(encoding="utf-8")

request_id_ctx: ContextVar[str] = ContextVar("request_id", default=None)
user_ctx: ContextVar[str] = ContextVar("user", default=None)


SENSITIVE_FIELDS = {"password", "token", "secret", "authorization"}


def mask_sensitive(data: dict | None):
    if not isinstance(data, dict):
        return data

    masked = {}
    for k, v in data.items():
        if k.lower() in SENSITIVE_FIELDS:
            masked[k] = "***"
        else:
            masked[k] = v
    return masked


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "ts": datetime.utcnow().isoformat() + "Z",
            "level": record.levelname,
            "logger": record.name,
            "msg": record.getMessage(),
            "module": record.module,
            "func": record.funcName,
            "line": record.lineno,
            "request_id": request_id_ctx.get(),
            "user": user_ctx.get(),
        }

        if hasattr(record, "extra_data"):
            log["data"] = mask_sensitive(record.extra_data)

        if record.exc_info:
            log["exception"] = {
                "type": record.exc_info[0].__name__,
                "msg": str(record.exc_info[1]),
                "stack": traceback.format_exception(*record.exc_info),
            }

        return json.dumps(log, ensure_ascii=False)


def setup_logger():
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    root.handlers.clear()
    root.addHandler(handler)

    return root


logger = setup_logger()
