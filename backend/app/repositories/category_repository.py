from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.repositories.base import BaseRepository
from app.models.category import Category

class CategoryRepository(BaseRepository[Category]) : 

    def __init__(self, session:Session):
        super().__init__(session, Category)

    def get_by_label(self, label: str) -> Category | None : 
        stmt = (
            select(Category).where(Category.label == label)
        )

        return self.session.scalars(stmt).first()

    def exists_by_label(self, label: str) -> bool: 

        return self.get_by_label(label) is not None

    def get_all_with_skills(self) -> list[Category]:
    
            stmt = (
                select(Category)
                .options(selectinload(Category.skills))
            )
    
            return self.session.scalars(stmt).all()