from uuid import UUID

from app.services import BaseService
from app.repositories import DomainRepository
from app.models import Domain
from app.schemas import DomainCreate, DomainUpdate


class DomainService(BaseService[Domain]):

    def __init__(self, repository: DomainRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: DomainCreate) -> Domain:
        entity = Domain(
            label=data.label,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[DomainCreate],
    ) -> list[Domain]:

        entities = [
            Domain(
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
        domain_id: UUID,
        data: DomainUpdate,
    ) -> Domain | None:

        entity = self.get_by_id(domain_id)

        if entity is None:
            return None

        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, domain_id: UUID) -> None:

        entity = self.get_by_id(domain_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()