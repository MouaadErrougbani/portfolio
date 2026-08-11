from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import DomainService
from app.repositories import DomainRepository
from app.db.dependencies import get_db
from app.schemas import (
    DomainCreate, DomainUpdate, DomainResponse
)

router = APIRouter(
    prefix="/domains",
    tags=["Domains"]
)
def get_domain_service(
        session: Session = Depends(get_db)
    ) -> DomainService: 
    return DomainService(DomainRepository(session=session))


@router.get(
    "/",
    response_model=list[DomainResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: DomainService = Depends(get_domain_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{domain_id}",
    response_model=DomainResponse,
    status_code=status.HTTP_200_OK,
)
def get_Domain(
    domain_id: UUID,
    service: DomainService = Depends(get_domain_service),
):
    return service.get_by_id(domain_id)


@router.post(
    "/",
    response_model=DomainResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Domain(
    data: DomainCreate,
    service: DomainService = Depends(get_domain_service),
):
    return service.create(data)


@router.patch(
    "/{domain_id}",
    response_model=DomainResponse,
    status_code=status.HTTP_200_OK,
)
def update_Domain(
    domain_id: UUID,
    data: DomainUpdate,
    service: DomainService = Depends(get_domain_service),
):    
    return service.update(domain_id=domain_id, data=data)


@router.delete(
    "/{domain_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Domain(
    domain_id: UUID,
    service: DomainService = Depends(get_domain_service),
):    
    service.delete(domain_id=domain_id)

# """