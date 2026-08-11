from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import ProgrammingLanguageService
from app.repositories import ProgrammingLanguageRepository
from app.db.dependencies import get_db
from app.schemas import (
    ProgrammingLanguageCreate, ProgrammingLanguageUpdate, ProgrammingLanguageResponse
)

router = APIRouter(
    prefix="/programming-languages",
    tags=["ProgrammingLanguages"]
)
def get_programming_language_service(
        session: Session = Depends(get_db)
    ) -> ProgrammingLanguageService: 
    return ProgrammingLanguageService(ProgrammingLanguageRepository(session=session))


@router.get(
    "/",
    response_model=list[ProgrammingLanguageResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: ProgrammingLanguageService = Depends(get_programming_language_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{programming_language_id}",
    response_model=ProgrammingLanguageResponse,
    status_code=status.HTTP_200_OK,
)
def get_ProgrammingLanguage(
    programming_language_id: UUID,
    service: ProgrammingLanguageService = Depends(get_programming_language_service),
):
    return service.get_by_id(programming_language_id)


@router.post(
    "/",
    response_model=ProgrammingLanguageResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_ProgrammingLanguage(
    data: ProgrammingLanguageCreate,
    service: ProgrammingLanguageService = Depends(get_programming_language_service),
):
    return service.create(data)


@router.patch(
    "/{programming_language_id}",
    response_model=ProgrammingLanguageResponse,
    status_code=status.HTTP_200_OK,
)
def update_ProgrammingLanguage(
    programming_language_id: UUID,
    data: ProgrammingLanguageUpdate,
    service: ProgrammingLanguageService = Depends(get_programming_language_service),
):    
    return service.update(programming_language_id=programming_language_id, data=data)


@router.delete(
    "/{programming_language_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_ProgrammingLanguage(
    programming_language_id: UUID,
    service: ProgrammingLanguageService = Depends(get_programming_language_service),
):    
    service.delete(programming_language_id=programming_language_id)
# """