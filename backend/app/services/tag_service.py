from uuid import UUID

from app.services import BaseService
from app.repositories import TagRepository
from app.models import Tag
from app.schemas import TagCreate, TagUpdate


class TagService(BaseService[Tag]):

    def __init__(self, repository: TagRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: TagCreate) -> Tag:
        entity = Tag(
            label=data.label,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[TagCreate],
    ) -> list[Tag]:

        entities = [
            Tag(
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
        tag_id: UUID,
        data: TagUpdate,
    ) -> Tag | None:

        entity = self.get_by_id(tag_id)

        if entity is None:
            return None

        entity.label = data.label

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, tag_id: UUID) -> None:

        entity = self.get_by_id(tag_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()