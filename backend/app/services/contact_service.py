from uuid import UUID

from app.services import BaseService
from app.repositories import ContactRepository
from app.models import Contact
from app.schemas import ContactCreate, ContactUpdate


class ContactService(BaseService[Contact]):

    def __init__(self, repository: ContactRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: ContactCreate) -> Contact:
        entity = Contact(
            label=data.label,
            icon=data.icon,
            link=data.link,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[ContactCreate],
    ) -> list[Contact]:

        entities = [
            Contact(
                label=item.label,
                icon=item.icon,
                link=item.link,
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
        contact_id: UUID,
        data: ContactUpdate,
    ) -> Contact | None:

        entity = self.get_by_id(contact_id)

        if entity is None:
            return None

        entity.label = data.label
        entity.icon = data.icon
        entity.link = data.link

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, contact_id: UUID) -> None:

        entity = self.get_by_id(contact_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()