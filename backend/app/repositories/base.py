from typing import Generic, TypeVar

from sqlalchemy.orm import Session
from sqlalchemy import select, func

from app.db.database import Base

ModelType = TypeVar("ModelType", bound=Base)

class BaseRepository(Generic[ModelType]):

    def __init__(self, session: Session, model: type[ModelType])->None:
        self.session = session
        self.model = model

    #============================
    # SELECT
    #============================

    def get_all(self)->list[ModelType] | None:
        stmt = select(self.model)

        return self.session.scalars(stmt).all()

    def get_by_id(self, entity_id) -> ModelType | None : 

        return self.session.get(self.model, entity_id) 

    def exists(self, entity_id) -> bool : 

        return self.get_by_id(entity_id) is not None 

    def count(self) -> int : 
        stmt = select(func.count()).select_from(self.model)

        return self.session.scalar(stmt)

    #============================
    # INSERT    
    #============================

    def create(self, entity: ModelType) -> ModelType: 
        self.session.add(entity)
        self.session.flush()
        self.session.refresh(entity)

        return entity

    def create_all(self, entitys: list[ModelType]) -> list[ModelType] :
        self.session.add_all(entitys) 
        self.session.flush()
        for entity in entitys :
            self.session.refresh(entity)
        
        return entitys
        
    #============================
    # UPDATE    
    #============================

    def update(self, entity: ModelType) -> ModelType : 
        self.session.flush()

        self.session.refresh(entity)


        return entity

    #============================
    # DELETE    
    #============================

    def delete(self, entity: ModelType) -> None : 
        self.session.delete(entity)
        self.session.flush()

    def commit(self) :
        self.session.commit()



