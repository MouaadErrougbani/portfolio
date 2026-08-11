from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import FrameworkService
from app.repositories import FrameworkRepository
from app.db.dependencies import get_db
from app.schemas import (
    FrameworkCreate, FrameworkUpdate, FrameworkResponse
)

router = APIRouter(
    prefix="/frameworks",
    tags=["Frameworks"]
)
def get_framework_service(
        session: Session = Depends(get_db)
    ) -> FrameworkService: 
    return FrameworkService(FrameworkRepository(session=session))


@router.get(
    "/",
    response_model=list[FrameworkResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: FrameworkService = Depends(get_framework_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{framework_id}",
    response_model=FrameworkResponse,
    status_code=status.HTTP_200_OK,
)
def get_Framework(
    framework_id: UUID,
    service: FrameworkService = Depends(get_framework_service),
):
    return service.get_by_id(framework_id)


@router.post(
    "/",
    response_model=FrameworkResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Framework(
    data: FrameworkCreate,
    service: FrameworkService = Depends(get_framework_service),
):
    return service.create(data)


@router.patch(
    "/{framework_id}",
    response_model=FrameworkResponse,
    status_code=status.HTTP_200_OK,
)
def update_Framework(
    framework_id: UUID,
    data: FrameworkUpdate,
    service: FrameworkService = Depends(get_framework_service),
):    
    return service.update(framework_id=framework_id, data=data)


@router.delete(
    "/{framework_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Framework(
    framework_id: UUID,
    service: FrameworkService = Depends(get_framework_service),
):    
    service.delete(framework_id=framework_id)

# """