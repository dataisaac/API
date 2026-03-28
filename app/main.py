import uvicorn
import time

from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.obervabilidade.logger import logger
from app.core.middlewares.middleware import ObservabilityMiddleware
from app.core.database.mysql_conn import get_db


# 1. Definição CORRETA do Lifespan (Apenas uma vez)
@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- STARTUP ---
    logger.info("--- Iniciando Ciclo de Vida da Aplicação ---")
    logger.info(f"Modo de Armazenamento: {settings.STORAGE_TYPE}")
    logger.info(f"DEBUG: Configurações carregadas -> {settings.model_dump()}")
    
    # Se quiser compartilhar o cliente S3 via state:
    app.state.db = get_db()
    # ou qualquer instancia de banco de dados
    yield  # <--- ESSENCIAL: A aplicação "mora" aqui
    
    # --- SHUTDOWN ---
    logger.info("--- Encerrando Ciclo de Vida da Aplicação ---")
    # Limpeza de recursos se necessário

def get_application() -> FastAPI:
    application = FastAPI(
        title="Persons API - ECS Production",
        description="API desacoplada para gerenciamento de pessoas usando S3/Parquet",
        lifespan=lifespan, # Referência para a função acima
        version="1.0.0",
        docs_url="/swagger",
        redoc_url="/documentacao",
        redirect_slashes=False 
    )

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @application.get("/health", tags=["Health"])
    async def health_check():
        return {"status": "healthy", "storage_type": settings.STORAGE_TYPE}

    application.include_router(api_router, prefix="/api/v1")

    return application

app = get_application()
app.add_middleware(ObservabilityMiddleware)

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    return Response(status_code=204) # 204 = No Content

# Middleware de Logs (Mantido como estava, está correto)
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    
    log_data = {
        "method": request.method,
        "path": request.url.path,
        "status_code": response.status_code,
        "duration_ms": round(process_time * 1000, 2)
    }
    logger.info(f"Request: {request.method} {request.url.path}", extra=log_data)
    return response