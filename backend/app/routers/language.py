from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import LanguageService
from app.repositories import LanguageRepository
from app.db.dependencies import get_db
from app.schemas import (
    LanguageCreate, LanguageUpdate, LanguageResponse
)

router = APIRouter(
    prefix="/languages",
    tags=["Languages"]
)
def get_language_service(
        session: Session = Depends(get_db)
    ) -> LanguageService: 
    return LanguageService(LanguageRepository(session=session))


@router.get(
    "/",
    response_model=list[LanguageResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: LanguageService = Depends(get_language_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{language_id}",
    response_model=LanguageResponse,
    status_code=status.HTTP_200_OK,
)
def get_Language(
    language_id: UUID,
    service: LanguageService = Depends(get_language_service),
):
    return service.get_by_id(language_id)


@router.post(
    "/",
    response_model=LanguageResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Language(
    data: LanguageCreate,
    service: LanguageService = Depends(get_language_service),
):
    return service.create(data)


@router.patch(
    "/{language_id}",
    response_model=LanguageResponse,
    status_code=status.HTTP_200_OK,
)
def update_Language(
    language_id: UUID,
    data: LanguageUpdate,
    service: LanguageService = Depends(get_language_service),
):    
    return service.update(language_id=language_id, data=data)


@router.delete(
    "/{language_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Language(
    language_id: UUID,
    service: LanguageService = Depends(get_language_service),
):    
    service.delete(language_id=language_id)


# """