from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import SubdomainService
from app.repositories import SubdomainRepository
from app.db.dependencies import get_db
from app.schemas import (
    SubdomainCreate, SubdomainUpdate, SubdomainResponse
)

router = APIRouter(
    prefix="/subdomains",
    tags=["Subdomains"]
)
def get_subdomain_service(
        session: Session = Depends(get_db)
    ) -> SubdomainService: 
    return SubdomainService(SubdomainRepository(session=session))


@router.get(
    "/",
    response_model=list[SubdomainResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: SubdomainService = Depends(get_subdomain_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{subdomain_id}",
    response_model=SubdomainResponse,
    status_code=status.HTTP_200_OK,
)
def get_Subdomain(
    subdomain_id: UUID,
    service: SubdomainService = Depends(get_subdomain_service),
):
    return service.get_by_id(subdomain_id)


@router.post(
    "/",
    response_model=SubdomainResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Subdomain(
    data: SubdomainCreate,
    service: SubdomainService = Depends(get_subdomain_service),
):
    return service.create(data)


@router.patch(
    "/{subdomain_id}",
    response_model=SubdomainResponse,
    status_code=status.HTTP_200_OK,
)
def update_Subdomain(
    subdomain_id: UUID,
    data: SubdomainUpdate,
    service: SubdomainService = Depends(get_subdomain_service),
):    
    return service.update(subdomain_id=subdomain_id, data=data)


@router.delete(
    "/{subdomain_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Subdomain(
    subdomain_id: UUID,
    service: SubdomainService = Depends(get_subdomain_service),
):    
    service.delete(subdomain_id=subdomain_id)

# """