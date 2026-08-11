from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import KeywordService
from app.repositories import KeywordRepository
from app.db.dependencies import get_db
from app.schemas import (
    KeywordCreate, KeywordUpdate, KeywordResponse
)

router = APIRouter(
    prefix="/keywords",
    tags=["Keywords"]
)
def get_keyword_service(
        session: Session = Depends(get_db)
    ) -> KeywordService: 
    return KeywordService(KeywordRepository(session=session))


@router.get(
    "/",
    response_model=list[KeywordResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: KeywordService = Depends(get_keyword_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{keyword_id}",
    response_model=KeywordResponse,
    status_code=status.HTTP_200_OK,
)
def get_Keyword(
    keyword_id: UUID,
    service: KeywordService = Depends(get_keyword_service),
):
    return service.get_by_id(keyword_id)


@router.post(
    "/",
    response_model=KeywordResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Keyword(
    data: KeywordCreate,
    service: KeywordService = Depends(get_keyword_service),
):
    return service.create(data)


@router.patch(
    "/{keyword_id}",
    response_model=KeywordResponse,
    status_code=status.HTTP_200_OK,
)
def update_Keyword(
    keyword_id: UUID,
    data: KeywordUpdate,
    service: KeywordService = Depends(get_keyword_service),
):    
    return service.update(keyword_id=keyword_id, data=data)


@router.delete(
    "/{keyword_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Keyword(
    keyword_id: UUID,
    service: KeywordService = Depends(get_keyword_service),
):    
    service.delete(keyword_id=keyword_id)

# """