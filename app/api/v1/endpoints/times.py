from fastapi import APIRouter, HTTPException, status, Depends
from app.api.v1.deps import get_time_service
from sqlalchemy.orm.session import Session
from app.core.database.mysql_conn import get_db
from app.schemas.times_create import TimeBase
from app.services.times_service import TimeService
from app.core.obervabilidade.logger import logger

router = APIRouter(
    prefix="/times",
    tags=["Times"],
    responses={404: {"description": "Not found"}}
)           

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_time(time: TimeBase, db: Session = Depends(get_db), response_model=TimeBase):
    try:
        service = get_time_service(db)
        return service.create_time(time)
    except Exception as e:
        logger.error(f"Erro ao criar: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
@router.put("/{id}", status_code=status.HTTP_200_OK)
async def update_time(id: int, time: TimeBase, db: Session = Depends(get_db)):
    try:
        service = get_time_service(db)
        return service.update_time(id, time)
    except Exception as e:
        logger.error(f"Erro ao atualizar: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    
@router.get("/list", status_code=status.HTTP_200_OK, response_model=list[TimeBase])
async def list_time(db: Session = Depends(get_db)):
    try:
        service = get_time_service(db)
        return service.list_all()
    except Exception as e:
        logger.error(f"Falha no endpoint de listagem: {str(e)}")
        raise HTTPException(
            status_code=500, # Use 500 para erros de infra (S3)
            detail=f"Erro interno ao acessar base de dados: {str(e)}"
        )
    
@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=TimeBase)
async def get_time(id: int, db: Session = Depends(get_db)):
    try:
        service = get_time_service(db)
        return service.get_time(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_time(id: int, db: Session = Depends(get_db)):
    try:
        service = get_time_service(db)
        return service.delete_time(id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
