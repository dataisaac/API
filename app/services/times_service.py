from app.repositories.base_repository import IBaseRepository
from app.schemas.times_create import TimeBase
import uuid

class TimeService:

    def __init__(self, repository: IBaseRepository):

        self.repository = repository

    def create_time(self, time_data: TimeBase):
        return self.repository.create(time_data)

    def list_all(self):

        return self.repository.get_all()
    
    def get_time(self, time_id):
        
        return self.repository.get(time_id)

    def update_time(self, time_id: int, time_data: TimeBase):
        
        return self.repository.update(time_data, time_id)

    def delete_time(self, time_id: int):
        
        return self.repository.delete(time_id)