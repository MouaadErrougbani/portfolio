from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import TraductionService
from app.repositories import TraductionRepository
from app.db.dependencies import get_db
from app.schemas import (
    TraductionCreate, TraductionUpdate, TraductionResponse
)

router = APIRouter(
    prefix="/traductions",
    tags=["Traductions"]
)
def get_traduction_service(
        session: Session = Depends(get_db)
    ) -> TraductionService: 
    return TraductionService(TraductionRepository(session=session))


@router.get(
    "/",
    response_model=list[TraductionResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: TraductionService = Depends(get_traduction_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{label}",
    response_model=TraductionResponse,
    status_code=status.HTTP_200_OK,
)
def get_Traduction(
    label: str,
    service: TraductionService = Depends(get_traduction_service),
):
    return service.get_by_id(label)


@router.post(
    "/",
    response_model=TraductionResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Traduction(
    data: TraductionCreate,
    service: TraductionService = Depends(get_traduction_service),
):
    return service.create(data)


@router.patch(
    "/{label}",
    response_model=TraductionResponse,
    status_code=status.HTTP_200_OK,
)
def update_Traduction(
    label: str,
    data: TraductionUpdate,
    service: TraductionService = Depends(get_traduction_service),
):    
    return service.update(label=label, data=data)


@router.delete(
    "/{label}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Traduction(
    label: str,
    service: TraductionService = Depends(get_traduction_service),
):    
    service.delete(label=label)

# """