from uuid import UUID

from app.services import BaseService
from app.repositories import DiplomaRepository
from app.models import Diploma
from app.schemas import DiplomaCreate, DiplomaUpdate


class DiplomaService(BaseService[Diploma]):

    def __init__(self, repository: DiplomaRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: DiplomaCreate) -> Diploma:
        entity = Diploma(
            name=data.name,
            establishment=data.establishment,
            start_date=data.start_date,
            end_date=data.end_date,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[DiplomaCreate],
    ) -> list[Diploma]:

        entities = [
            Diploma(
                name=item.name,
                establishment=item.establishment,
                start_date=item.start_date,
                end_date=item.end_date,
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
        diploma_id: UUID,
        data: DiplomaUpdate,
    ) -> Diploma | None:

        entity = self.get_by_id(diploma_id)

        if entity is None:
            return None

        entity.name = data.name
        entity.establishment = data.establishment
        entity.start_date = data.start_date
        entity.end_date = data.end_date

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, diploma_id: UUID) -> None:

        entity = self.get_by_id(diploma_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()