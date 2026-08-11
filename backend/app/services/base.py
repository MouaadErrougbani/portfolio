from typing import Generic, TypeVar
from abc import abstractmethod

from app.db.database import Base
from app.repositories import BaseRepository

ModelType = TypeVar("ModelType", bound=Base)

class BaseService(Generic[ModelType]) : 
    def __init__(self, repository: BaseRepository[ModelType]) -> None:
        self.repository = repository

    #==========================
    # SELECT
    #==========================

    def get_all(self)->list[ModelType] | None : 
        return self.repository.get_all()

    def get_by_id(self, entity_id) -> ModelType | None : 
        return self.repository.get_by_id(entity_id=entity_id)

    def exists(self, entity_id) -> bool : 
        return self.repository.exists(entity_id=entity_id)

    def count(self) -> int: 
        return self.repository.count()

    def commit(self) -> None : 
        self.repository.commit()

    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def create_all(self, data):
        pass

    @abstractmethod
    def update(self, id, data):
        pass

    @abstractmethod
    def delete(self, id):
        pass
