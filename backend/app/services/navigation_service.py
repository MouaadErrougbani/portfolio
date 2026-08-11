from uuid import UUID

from app.services import BaseService
from app.repositories import NavigationRepository
from app.models import Navigation
from app.schemas import NavigationCreate, NavigationUpdate


class NavigationService(BaseService[Navigation]):

    def __init__(self, repository: NavigationRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: NavigationCreate) -> Navigation:
        entity = Navigation(
            label=data.label,
            enabled=data.enabled,
            position=data.position,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[NavigationCreate],
    ) -> list[Navigation]:

        entities = [
            Navigation(
                label=item.label,
                enabled=item.enabled,
                position=item.position,
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
        navigation_id: UUID,
        data: NavigationUpdate,
    ) -> Navigation | None:

        entity = self.get_by_id(navigation_id)

        if entity is None:
            return None

        entity.label = data.label
        entity.enabled = data.enabled
        entity.position = data.position

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, navigation_id: UUID) -> None:

        entity = self.get_by_id(navigation_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()