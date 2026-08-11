from uuid import UUID

from app.services import BaseService
from app.repositories import ProgrammingLanguageRepository
from app.models import ProgrammingLanguage
from app.schemas import ProgrammingLanguageCreate, ProgrammingLanguageUpdate


class ProgrammingLanguageService(BaseService[ProgrammingLanguage]):

    def __init__(
        self,
        repository: ProgrammingLanguageRepository,
    ) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(
        self,
        data: ProgrammingLanguageCreate,
    ) -> ProgrammingLanguage:

        entity = ProgrammingLanguage(
            label=data.label,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[ProgrammingLanguageCreate],
    ) -> list[ProgrammingLanguage]:

        entities = [
            ProgrammingLanguage(
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
        programming_language_id: UUID,
        data: ProgrammingLanguageUpdate,
    ) -> ProgrammingLanguage | None:

        entity = self.get_by_id(programming_language_id)

        if entity is None:
            return None

        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(
        self,
        programming_language_id: UUID,
    ) -> None:

        entity = self.get_by_id(programming_language_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()