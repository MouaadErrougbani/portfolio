from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import ContactService
from app.repositories import ContactRepository
from app.db.dependencies import get_db
from app.schemas import (
    ContactCreate, ContactUpdate, ContactResponse
)

router = APIRouter(
    prefix="/contacts",
    tags=["Contacts"]
)
def get_contact_service(
        session: Session = Depends(get_db)
    ) -> ContactService: 
    return ContactService(ContactRepository(session=session))


@router.get(
    "/",
    response_model=list[ContactResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: ContactService = Depends(get_contact_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{contact_id}",
    response_model=ContactResponse,
    status_code=status.HTTP_200_OK,
)
def get_Contact(
    contact_id: UUID,
    service: ContactService = Depends(get_contact_service),
):
    return service.get_by_id(contact_id)


@router.post(
    "/",
    response_model=ContactResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Contact(
    data: ContactCreate,
    service: ContactService = Depends(get_contact_service),
):
    return service.create(data)


@router.patch(
    "/{contact_id}",
    response_model=ContactResponse,
    status_code=status.HTTP_200_OK,
)
def update_Contact(
    contact_id: UUID,
    data: ContactUpdate,
    service: ContactService = Depends(get_contact_service),
):    
    return service.update(contact_id=contact_id, data=data)


@router.delete(
    "/{contact_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Contact(
    contact_id: UUID,
    service: ContactService = Depends(get_contact_service),
):    
    service.delete(contact_id=contact_id)

#"""