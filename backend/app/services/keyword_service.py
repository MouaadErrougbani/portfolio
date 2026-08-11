from uuid import UUID

from app.services import BaseService
from app.repositories import KeywordRepository
from app.models import Keyword
from app.schemas import KeywordCreate, KeywordUpdate


class KeywordService(BaseService[Keyword]):

    def __init__(self, repository: KeywordRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: KeywordCreate) -> Keyword:
        entity = Keyword(
            label=data.label,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[KeywordCreate],
    ) -> list[Keyword]:

        entities = [
            Keyword(
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
        keyword_id: UUID,
        data: KeywordUpdate,
    ) -> Keyword | None:

        entity = self.get_by_id(keyword_id)

        if entity is None:
            return None

        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, keyword_id: UUID) -> None:

        entity = self.get_by_id(keyword_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()