from uuid import UUID

from app.services import BaseService
from app.repositories import SubdomainRepository
from app.models import Subdomain
from app.schemas import SubdomainCreate, SubdomainUpdate


class SubdomainService(BaseService[Subdomain]):

    def __init__(self, repository: SubdomainRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: SubdomainCreate) -> Subdomain:
        entity = Subdomain(
            label=data.label,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[SubdomainCreate],
    ) -> list[Subdomain]:

        entities = [
            Subdomain(
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
        subdomain_id: UUID,
        data: SubdomainUpdate,
    ) -> Subdomain | None:

        entity = self.get_by_id(subdomain_id)

        if entity is None:
            return None

        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, subdomain_id: UUID) -> None:

        entity = self.get_by_id(subdomain_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()