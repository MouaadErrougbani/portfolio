from sqlalchemy import (
    Column,
    ForeignKeyConstraint,
    PrimaryKeyConstraint,
    Table,
    Uuid,
)

from app.db.database import Base

metadata = Base.metadata


project_framework = Table(
    "project_framework",
    metadata,
    Column("id_project", Uuid, nullable=False),
    Column("id_framework", Uuid, nullable=False),
    ForeignKeyConstraint(
        ["id_project"],
        ["projects.id"],
        name="project_framework_id_project_fkey",
    ),
    ForeignKeyConstraint(
        ["id_framework"],
        ["frameworks.id"],
        name="project_framework_id_framework_fkey",
    ),
    PrimaryKeyConstraint(
        "id_project",
        "id_framework",
        name="project_framework_pkey",
    ),
)


project_keyword = Table(
    "project_keyword",
    metadata,
    Column("id_project", Uuid, nullable=False),
    Column("id_keyword", Uuid, nullable=False),
    ForeignKeyConstraint(
        ["id_project"],
        ["projects.id"],
        name="project_keyword_id_project_fkey",
    ),
    ForeignKeyConstraint(
        ["id_keyword"],
        ["keywords.id"],
        name="project_keyword_id_keyword_fkey",
    ),
    PrimaryKeyConstraint(
        "id_project",
        "id_keyword",
        name="project_keyword_pkey",
    ),
)


project_language = Table(
    "project_language",
    metadata,
    Column("id_project", Uuid, nullable=False),
    Column("id_programming_language", Uuid, nullable=False),
    ForeignKeyConstraint(
        ["id_project"],
        ["projects.id"],
        name="project_language_id_project_fkey",
    ),
    ForeignKeyConstraint(
        ["id_programming_language"],
        ["programming_languages.id"],
        name="project_language_id_programming_language_fkey",
    ),
    PrimaryKeyConstraint(
        "id_project",
        "id_programming_language",
        name="project_language_pkey",
    ),
)


project_subdomain = Table(
    "project_subdomain",
    metadata,
    Column("id_project", Uuid, nullable=False),
    Column("id_subdomain", Uuid, nullable=False),
    ForeignKeyConstraint(
        ["id_project"],
        ["projects.id"],
        name="project_subdomain_id_project_fkey",
    ),
    ForeignKeyConstraint(
        ["id_subdomain"],
        ["subdomains.id"],
        name="project_subdomain_id_subdomain_fkey",
    ),
    PrimaryKeyConstraint(
        "id_project",
        "id_subdomain",
        name="project_subdomain_pkey",
    ),
)


project_tag = Table(
    "project_tag",
    metadata,
    Column("id_project", Uuid, nullable=False),
    Column("id_tag", Uuid, nullable=False),
    ForeignKeyConstraint(
        ["id_project"],
        ["projects.id"],
        name="project_tag_id_project_fkey",
    ),
    ForeignKeyConstraint(
        ["id_tag"],
        ["tags.id"],
        name="project_tag_id_tag_fkey",
    ),
    PrimaryKeyConstraint(
        "id_project",
        "id_tag",
        name="project_tag_pkey",
    ),
)