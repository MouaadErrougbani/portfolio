from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import NavigationService
from app.repositories import NavigationRepository
from app.db.dependencies import get_db
from app.schemas import (
    NavigationCreate, NavigationUpdate, NavigationResponse
)

router = APIRouter(
    prefix="/navigations",
    tags=["Navigations"]
)
def get_navigation_service(
        session: Session = Depends(get_db)
    ) -> NavigationService: 
    return NavigationService(NavigationRepository(session=session))


@router.get(
    "/",
    response_model=list[NavigationResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: NavigationService = Depends(get_navigation_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{navigation_id}",
    response_model=NavigationResponse,
    status_code=status.HTTP_200_OK,
)
def get_Navigation(
    navigation_id: UUID,
    service: NavigationService = Depends(get_navigation_service),
):
    return service.get_by_id(navigation_id)


@router.post(
    "/",
    response_model=NavigationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Navigation(
    data: NavigationCreate,
    service: NavigationService = Depends(get_navigation_service),
):
    return service.create(data)


@router.patch(
    "/{navigation_id}",
    response_model=NavigationResponse,
    status_code=status.HTTP_200_OK,
)
def update_Navigation(
    navigation_id: UUID,
    data: NavigationUpdate,
    service: NavigationService = Depends(get_navigation_service),
):    
    return service.update(navigation_id=navigation_id, data=data)


@router.delete(
    "/{navigation_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Navigation(
    navigation_id: UUID,
    service: NavigationService = Depends(get_navigation_service),
):    
    service.delete(navigation_id=navigation_id)

# """