from uuid import UUID

from app.services import BaseService
from app.repositories import ProjectRepository
from app.models import Project
from app.schemas import ProjectCreate, ProjectUpdate


class ProjectService(BaseService[Project]):

    def __init__(self, repository: ProjectRepository) -> None:
        super().__init__(repository)

    # ==========================
    # INSERT
    # ==========================

    def create(self, data: ProjectCreate) -> Project:
        entity = Project(
            name=data.name,
            description=data.description,
            github_link=data.github_link,
            production_link=data.production_link,
            realization_date=data.realization_date,
            image=data.image,
            id_domain=data.id_domain,
        )

        entity = self.repository.create(entity=entity)

        self.commit()

        return entity

    def create_all(
        self,
        data: list[ProjectCreate],
    ) -> list[Project]:

        entities = [
            Project(
                name=item.name,
                description=item.description,
                github_link=item.github_link,
                production_link=item.production_link,
                realization_date=item.realization_date,
                image=item.image,
                id_domain=item.id_domain,
            )
            for item in data
        ]

        entities = self.repository.create_all(entities=entities)

        self.commit()

        return entities

    # ==========================
    # UPDATE
    # ==========================

    def update(
        self,
        project_id: UUID,
        data: ProjectUpdate,
    ) -> Project | None:

        entity = self.get_by_id(project_id)

        if entity is None:
            return None

        entity.name = data.name
        entity.description = data.description
        entity.github_link = data.github_link
        entity.production_link = data.production_link
        entity.realization_date = data.realization_date
        entity.image = data.image
        entity.id_domain = data.id_domain

        entity = self.repository.update(entity=entity)

        self.commit()

        return entity

    # ==========================
    # DELETE
    # ==========================

    def delete(self, project_id: UUID) -> None:

        entity = self.get_by_id(project_id)

        if entity is None:
            return

        self.repository.delete(entity=entity)

        self.commit()

    def get_all_with_details(self) -> list[dict]:

        projects = self.repository.get_all_with_details()

        return [
            {
                "id": project.id,
                "name": project.name,
                "description": project.description,

                "tags": [
                    tag.label
                    for tag in project.tags
                ],

                "githubLink": project.github_link,
                "productionLink": project.production_link,

                "realizationDate": project.realization_date,

                "domain": (
                    project.domain.label
                    if project.domain
                    else None
                ),

                "subDomain": [
                    subdomain.label
                    for subdomain in project.subdomains
                ],

                "keywords": [
                    keyword.label
                    for keyword in project.keywords
                ],

                "languages": [
                    language.label
                    for language in project.programming_languages
                ],

                "frameworks": [
                    framework.label
                    for framework in project.frameworks
                ],

                "image": project.image,
            }
            for project in projects
        ]

