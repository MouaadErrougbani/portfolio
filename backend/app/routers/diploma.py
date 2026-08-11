from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import DiplomaService
from app.repositories import DiplomaRepository
from app.db.dependencies import get_db
from app.schemas import (
    DiplomaCreate, DiplomaUpdate, DiplomaResponse
)

router = APIRouter(
    prefix="/diplomas",
    tags=["Diplomas"]
)
def get_diploma_service(
        session: Session = Depends(get_db)
    ) -> DiplomaService: 
    return DiplomaService(DiplomaRepository(session=session))


@router.get(
    "/",
    response_model=list[DiplomaResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: DiplomaService = Depends(get_diploma_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{diploma_id}",
    response_model=DiplomaResponse,
    status_code=status.HTTP_200_OK,
)
def get_Diploma(
    diploma_id: UUID,
    service: DiplomaService = Depends(get_diploma_service),
):
    return service.get_by_id(diploma_id)


@router.post(
    "/",
    response_model=DiplomaResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Diploma(
    data: DiplomaCreate,
    service: DiplomaService = Depends(get_diploma_service),
):
    return service.create(data)


@router.patch(
    "/{diploma_id}",
    response_model=DiplomaResponse,
    status_code=status.HTTP_200_OK,
)
def update_Diploma(
    diploma_id: UUID,
    data: DiplomaUpdate,
    service: DiplomaService = Depends(get_diploma_service),
):    
    return service.update(diploma_id=diploma_id, data=data)


@router.delete(
    "/{diploma_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Diploma(
    diploma_id: UUID,
    service: DiplomaService = Depends(get_diploma_service),
):    
    service.delete(diploma_id=diploma_id)

# """