from abc import ABC, abstractmethod

class IBaseRepository(ABC):

    @abstractmethod
    def create(self, time_data: dict) -> dict:
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def get(self, id: str) -> dict:
        pass
    
    @abstractmethod
    def update(self, person_data: dict, id: str) -> dict:
        pass

    @abstractmethod
    def delete(self, id: str) -> dict:
        pass