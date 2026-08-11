from uuid import UUID

from app.models import Category
from app.repositories import CategoryRepository
from app.schemas import CategoryCreate, CategoryUpdate
from app.services import BaseService


class CategoryService(BaseService[Category]):

    def __init__(self, repository: CategoryRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: CategoryCreate) -> Category:
        entity = Category(
            label=data.label
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(self, data: list[CategoryCreate]) -> list[Category]:
        entities = [
            Category(label=item.label)
            for item in data
        ]

        entities = self.repository.create_all(entities=entities)

        self.commit()

        return entities

    # ==========================
    # UPDATE
    # ==========================

    def update(
        self,
        category_id: UUID,
        data: CategoryUpdate,
    ) -> Category | None:

        entity = self.get_by_id(category_id)

        if entity is None:
            return None

        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, category_id: UUID) -> None:

        entity = self.get_by_id(category_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()

    # ==========================
    # CUSTOM SELECT
    # ==========================

    def get_by_label(self, label: str) -> Category | None:
        return self.repository.get_by_label(label=label)

    def exists_by_label(self, label: str) -> bool:
        return self.repository.exists_by_label(label=label)

    def get_all_with_skills(self) -> dict[str, list[str]]:
    
        categories = self.repository.get_all_with_skills()

        return {
            category.label: [
                skill.skill
                for skill in category.skills
            ]
            for category in categories
        }