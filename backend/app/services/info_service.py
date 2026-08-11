from app.services import BaseService
from app.repositories import InfoRepository
from app.models import Info
from app.schemas import InfoCreate, InfoUpdate


class InfoService(BaseService[Info]):

    def __init__(self, repository: InfoRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: InfoCreate) -> Info:
        entity = Info(
            id=data.id,
            message=data.message,
            petit_desc=data.petit_desc,
            full_desc=data.full_desc,
            image=data.image,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[InfoCreate],
    ) -> list[Info]:

        entities = [
            Info(
                id=item.id,
                message=item.message,
                petit_desc=item.petit_desc,
                full_desc=item.full_desc,
                image=item.image,
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
        info_id: int,
        data: InfoUpdate,
    ) -> Info | None:

        entity = self.get_by_id(info_id)

        if entity is None:
            return None

        entity.message = data.message
        entity.petit_desc = data.petit_desc
        entity.full_desc = data.full_desc
        entity.image = data.image

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, info_id: int) -> None:

        entity = self.get_by_id(info_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()