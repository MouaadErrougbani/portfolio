from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import SkillService
from app.repositories import SkillRepository
from app.db.dependencies import get_db
from app.schemas import (
    SkillCreate, SkillUpdate, SkillResponse
)

router = APIRouter(
    prefix="/skills",
    tags=["Skills"]
)
def get_skill_service(
        session: Session = Depends(get_db)
    ) -> SkillService: 
    return SkillService(SkillRepository(session=session))


@router.get(
    "/",
    response_model=list[SkillResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: SkillService = Depends(get_skill_service),
):
    return service.get_all()

_ = """
@router.get(
    "/{skill_id}",
    response_model=SkillResponse,
    status_code=status.HTTP_200_OK,
)
def get_Skill(
    skill_id: UUID,
    service: SkillService = Depends(get_skill_service),
):
    return service.get_by_id(skill_id)


@router.post(
    "/",
    response_model=SkillResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Skill(
    data: SkillCreate,
    service: SkillService = Depends(get_skill_service),
):
    return service.create(data)


@router.patch(
    "/{skill_id}",
    response_model=SkillResponse,
    status_code=status.HTTP_200_OK,
)
def update_Skill(
    skill_id: UUID,
    data: SkillUpdate,
    service: SkillService = Depends(get_skill_service),
):    
    return service.update(skill_id=skill_id, data=data)


@router.delete(
    "/{skill_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Skill(
    skill_id: UUID,
    service: SkillService = Depends(get_skill_service),
):    
    service.delete(skill_id=skill_id)

# """