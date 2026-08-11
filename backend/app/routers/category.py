from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.db.dependencies import get_db
from app.schemas import (
    CategoryCreate,
    CategoryResponse,
    CategoryUpdate,
    SkillsByCategoryResponse
)
from app.services import CategoryService
from app.repositories import CategoryRepository

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
)


def get_category_service(
    session: Session = Depends(get_db),
) -> CategoryService:
    return CategoryService(CategoryRepository(session))


@router.get(
    "/",
    response_model=list[CategoryResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: CategoryService = Depends(get_category_service),
):
    return service.get_all()

@router.get(
    "/with-skills",
    response_model=SkillsByCategoryResponse,
    status_code=status.HTTP_200_OK,
)
def get_categories_with_skills(
    service: CategoryService = Depends(get_category_service),
):
    return service.get_all_with_skills()

_ = """
@router.get(
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
)
def get_category(
    category_id: UUID,
    service: CategoryService = Depends(get_category_service),
):
    return service.get_by_id(category_id)


@router.post(
    "/",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_category(
    data: CategoryCreate,
    service: CategoryService = Depends(get_category_service),
):
    return service.create(data)


@router.patch(
    "/{category_id}",
    response_model=CategoryResponse,
    status_code=status.HTTP_200_OK,
)
def update_category(
    category_id: UUID,
    data: CategoryUpdate,
    service: CategoryService = Depends(get_category_service),
):    
    return service.update(category_id=category_id, data=data)


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_category(
    category_id: UUID,
    service: CategoryService = Depends(get_category_service),
):    
    service.delete(category_id=category_id)

#"""