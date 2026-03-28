from app.repositories.brasileirao.times_repository import TimesRepository
from app.services.times_service import TimeService
from sqlalchemy.orm.session import Session
from app.core.config import settings
from fastapi import Request

def get_time_service(database: Session) -> TimeService:
    # MUDANÇA DE FONTE DE DADOS AQUI:
    storage_type = settings.STORAGE_TYPE
    
    if storage_type == "MYSQL":
        repo = TimesRepository(database=database)  # Usando o banco de dados compartilhado via state
    else:
        raise NotImplementedError("Storage type not supported yet")
        
    return TimeService(repo)