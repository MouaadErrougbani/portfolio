from uuid import UUID

from app.services import BaseService
from app.repositories import SkillRepository
from app.models import Skill
from app.schemas import SkillCreate, SkillUpdate


class SkillService(BaseService[Skill]):

    def __init__(self, repository: SkillRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: SkillCreate) -> Skill:
        entity = Skill(
            skill=data.skill,
            category_id=data.category_id,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[SkillCreate],
    ) -> list[Skill]:

        entities = [
            Skill(
                skill=item.skill,
                category_id=item.category_id,
            )
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
        skill_id: UUID,
        data: SkillUpdate,
    ) -> Skill | None:

        entity = self.get_by_id(skill_id)

        if entity is None:
            return None

        entity.skill = data.skill
        entity.category_id = data.category_id

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, skill_id: UUID) -> None:

        entity = self.get_by_id(skill_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()

