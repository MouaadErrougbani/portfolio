from app.services import BaseService
from app.repositories import TraductionRepository
from app.models import Traduction
from app.schemas import TraductionCreate, TraductionUpdate


class TraductionService(BaseService[Traduction]):

    def __init__(self, repository: TraductionRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: TraductionCreate) -> Traduction:
        entity = Traduction(
            label=data.label,
            ar=data.ar,
            fr=data.fr,
            en=data.en,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[TraductionCreate],
    ) -> list[Traduction]:

        entities = [
            Traduction(
                label=item.label,
                ar=item.ar,
                fr=item.fr,
                en=item.en,
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
        label: str,
        data: TraductionUpdate,
    ) -> Traduction | None:

        entity = self.get_by_id(label)

        if entity is None:
            return None

        entity.ar = data.ar
        entity.fr = data.fr
        entity.en = data.en

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, label: str) -> None:

        entity = self.get_by_id(label)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()