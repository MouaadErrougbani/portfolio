from uuid import UUID

from app.services import BaseService
from app.repositories import LanguageRepository
from app.models import Language
from app.schemas import LanguageCreate, LanguageUpdate


class LanguageService(BaseService[Language]):

    def __init__(self, repository: LanguageRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: LanguageCreate) -> Language:
        entity = Language(
            code=data.code,
            label=data.label,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[LanguageCreate],
    ) -> list[Language]:

        entities = [
            Language(
                code=item.code,
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
        language_id: UUID,
        data: LanguageUpdate,
    ) -> Language | None:

        entity = self.get_by_id(language_id)

        if entity is None:
            return None

        entity.code = data.code
        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, language_id: UUID) -> None:

        entity = self.get_by_id(language_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()