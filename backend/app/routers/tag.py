from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import TagService
from app.repositories import TagRepository
from app.db.dependencies import get_db
from app.schemas import (
    TagCreate, TagUpdate, TagResponse
)

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)
def get_tag_service(
        session: Session = Depends(get_db)
    ) -> TagService: 
    return TagService(TagRepository(session=session))


@router.get(
    "/",
    response_model=list[TagResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: TagService = Depends(get_tag_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{tag_id}",
    response_model=TagResponse,
    status_code=status.HTTP_200_OK,
)
def get_Tag(
    tag_id: UUID,
    service: TagService = Depends(get_tag_service),
):
    return service.get_by_id(tag_id)


@router.post(
    "/",
    response_model=TagResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Tag(
    data: TagCreate,
    service: TagService = Depends(get_tag_service),
):
    return service.create(data)


@router.patch(
    "/{tag_id}",
    response_model=TagResponse,
    status_code=status.HTTP_200_OK,
)
def update_Tag(
    tag_id: UUID,
    data: TagUpdate,
    service: TagService = Depends(get_tag_service),
):    
    return service.update(tag_id=tag_id, data=data)


@router.delete(
    "/{tag_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Tag(
    tag_id: UUID,
    service: TagService = Depends(get_tag_service),
):    
    service.delete(tag_id=tag_id)

# """