from sqlalchemy.orm import Session, selectinload
from sqlalchemy import select

from app.models import Project
from app.repositories import BaseRepository

class ProjectRepository(BaseRepository[Project]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Project)
    def get_all_with_details(self) -> list[Project]:

        stmt = (
            select(Project)
            .options(
                selectinload(Project.domain),
                selectinload(Project.tags),
                selectinload(Project.subdomains),
                selectinload(Project.keywords),
                selectinload(Project.programming_languages),
                selectinload(Project.frameworks),
            )
        )

        return self.session.scalars(stmt).all()