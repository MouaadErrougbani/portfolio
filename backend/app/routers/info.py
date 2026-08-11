from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import InfoService
from app.repositories import InfoRepository
from app.db.dependencies import get_db
from app.schemas import (
    InfoCreate, InfoUpdate, InfoResponse
)

router = APIRouter(
    prefix="/infos",
    tags=["Infos"]
)
def get_info_service(
        session: Session = Depends(get_db)
    ) -> InfoService: 
    return InfoService(InfoRepository(session=session))


@router.get(
    "/",
    response_model=list[InfoResponse],
    status_code=status.HTTP_200_OK,
)
def get_infos(
    service: InfoService = Depends(get_info_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{info_id}",
    response_model=InfoResponse,
    status_code=status.HTTP_200_OK,
)
def get_Info(
    info_id: int,
    service: InfoService = Depends(get_info_service),
):
    return service.get_by_id(info_id)


@router.post(
    "/",
    response_model=InfoResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Info(
    data: InfoCreate,
    service: InfoService = Depends(get_info_service),
):
    return service.create(data)


@router.patch(
    "/{info_id}",
    response_model=InfoResponse,
    status_code=status.HTTP_200_OK,
)
def update_Info(
    info_id: int,
    data: InfoUpdate,
    service: InfoService = Depends(get_info_service),
):    
    return service.update(info_id=info_id, data=data)


@router.delete(
    "/{info_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Info(
    info_id: int,
    service: InfoService = Depends(get_info_service),
):    
    service.delete(info_id=info_id)

# """