from uuid import UUID

from app.services import BaseService
from app.repositories import FrameworkRepository
from app.models import Framework
from app.schemas import FrameworkCreate, FrameworkUpdate


class FrameworkService(BaseService[Framework]):

    def __init__(self, repository: FrameworkRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: FrameworkCreate) -> Framework:
        entity = Framework(
            label=data.label,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[FrameworkCreate],
    ) -> list[Framework]:

        entities = [
            Framework(
                label=item.label,
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
        framework_id: UUID,
        data: FrameworkUpdate,
    ) -> Framework | None:

        entity = self.get_by_id(framework_id)

        if entity is None:
            return None

        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, framework_id: UUID) -> None:

        entity = self.get_by_id(framework_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()