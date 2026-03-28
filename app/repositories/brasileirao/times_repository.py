from app.models.times import Times
from app.repositories.base_repository import IBaseRepository
from app.core.obervabilidade.logger import logger
from app.core.config import settings
from app.schemas.times_create import TimeBase

class TimesRepository(IBaseRepository):

    def __init__(self, database=None):
        self.__database = database

    def create(self, time_data: TimeBase) -> dict:

        try:

            model = time_data.model_dump()
            model = Times(**model)  # Converte o Pydantic para o modelo SQLAlchemy
            self.__database.add(model)
            self.__database.commit()
            self.__database.refresh(model)
            
            return model
        
        except Exception as e:
            logger.exception("Falha crítica ao criar Time: %s", str(e))
            raise e


    def get_all(self) -> list:
        
        try:
            return self.__database.query(Times).all()
        except Exception as e:
            logger.error(f"Erro ao listar Times: {str(e)}", exc_info=True)
            raise e

    def get(self, id: str) -> dict:
        
        try:
            return self.__database.query(Times).filter(Times.id == id).first()
        except Exception as e:
            logger.error(f"Erro ao listar Times: {str(e)}")
            raise e

    
    def update(self, time_data: TimeBase, id: str) -> dict:

        try:

            time = self.__database.query(Times).filter(Times.id == id).first()

            if not time:
                raise ValueError(f"Time com id {id} não encontrado")
            
            time.name = time_data.name
            
            self.__database.add(time)
            self.__database.commit()
            self.__database.refresh(time)

            return time
        
        except Exception as e:
            logger.error(f"Erro ao atualizar Time: {str(e)}")
            raise e

    def delete(self, id: str) -> dict:
        
        try:
            time = self.__database.query(Times).filter(Times.id == id).first()

            if not time:
                raise ValueError(f"Time com id {id} não encontrado")
            
            self.__database.delete(time)
            self.__database.commit()

            return {"message": f"Time com id {id} deletado com sucesso"}
        except Exception as e:
            logger.error(f"Erro ao deletar Time: {str(e)}")
            raise e