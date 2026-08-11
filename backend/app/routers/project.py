from uuid import UUID

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.services import ProjectService
from app.repositories import ProjectRepository
from app.db.dependencies import get_db
from app.schemas import (
    ProjectCreate, ProjectUpdate, ProjectResponse, ProjectDetailsResponse
)

router = APIRouter(
    prefix="/projects",
    tags=["Projects"]
)
def get_project_service(
        session: Session = Depends(get_db)
    ) -> ProjectService: 
    return ProjectService(ProjectRepository(session=session))


@router.get(
    "/",
    response_model=list[ProjectResponse],
    status_code=status.HTTP_200_OK,
)
def get_categories(
    service: ProjectService = Depends(get_project_service),
):
    return service.get_all()

@router.get(
    "/with-details",
    response_model=list[ProjectDetailsResponse],
    status_code=status.HTTP_200_OK,
)
def get_projects_with_details(
    service: ProjectService = Depends(get_project_service),
):
    return service.get_all_with_details()
_ = """
@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
def get_Project(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
):
    return service.get_by_id(project_id)


@router.post(
    "/",
    response_model=ProjectResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_Project(
    data: ProjectCreate,
    service: ProjectService = Depends(get_project_service),
):
    return service.create(data)


@router.patch(
    "/{project_id}",
    response_model=ProjectResponse,
    status_code=status.HTTP_200_OK,
)
def update_Project(
    project_id: UUID,
    data: ProjectUpdate,
    service: ProjectService = Depends(get_project_service),
):    
    return service.update(project_id=project_id, data=data)


@router.delete(
    "/{project_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_Project(
    project_id: UUID,
    service: ProjectService = Depends(get_project_service),
):    
    service.delete(project_id=project_id)


# """