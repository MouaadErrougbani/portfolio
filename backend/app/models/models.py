from typing import List, Optional

from sqlalchemy import Boolean, Column, Date, ForeignKeyConstraint, PrimaryKeyConstraint, SmallInteger, String, Table, Text, UniqueConstraint, Uuid, text
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, relationship
from sqlalchemy.orm.base import Mapped

Base = declarative_base()
metadata = Base.metadata


class Categories(Base):
    __tablename__ = 'categories'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='categories_pkey'),
        UniqueConstraint('label', name='categories_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)

    skills: Mapped[List['Skills']] = relationship('Skills', uselist=True, back_populates='category')


class Contacts(Base):
    __tablename__ = 'contacts'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='contacts_pkey'),
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)
    icon = mapped_column(Text)
    link = mapped_column(Text)


class Diplomas(Base):
    __tablename__ = 'diplomas'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='diplomas_pkey'),
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    name = mapped_column(Text, nullable=False)
    establishment = mapped_column(Text, nullable=False)
    start_date = mapped_column(Date)
    end_date = mapped_column(Date)


class Domains(Base):
    __tablename__ = 'domains'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='domains_pkey'),
        UniqueConstraint('label', name='domains_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)

    projects: Mapped[List['Projects']] = relationship('Projects', uselist=True, back_populates='domains')


class Frameworks(Base):
    __tablename__ = 'frameworks'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='frameworks_pkey'),
        UniqueConstraint('label', name='frameworks_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)

    projects: Mapped['Projects'] = relationship('Projects', secondary='project_framework', back_populates='frameworks')


class Infos(Base):
    __tablename__ = 'infos'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='infos_pkey'),
    )

    id = mapped_column(SmallInteger, server_default=text('1'))
    message = mapped_column(Text)
    petit_desc = mapped_column(Text)
    full_desc = mapped_column(Text)
    image = mapped_column(Text)


class Keywords(Base):
    __tablename__ = 'keywords'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='keywords_pkey'),
        UniqueConstraint('label', name='keywords_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)

    projects: Mapped['Projects'] = relationship('Projects', secondary='project_keyword', back_populates='keywords')


class Languages(Base):
    __tablename__ = 'languages'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='languages_pkey'),
        UniqueConstraint('code', name='languages_code_key'),
        UniqueConstraint('label', name='languages_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    code = mapped_column(Text, nullable=False)
    label = mapped_column(Text, nullable=False)


t_my_users = Table(
    'my_users', metadata,
    Column('name', String),
    Column('add', String)
)


class Navigations(Base):
    __tablename__ = 'navigations'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='navigations_pkey'),
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)
    position = mapped_column(SmallInteger, nullable=False)
    enabled = mapped_column(Boolean, server_default=text('true'))


class ProgrammingLanguages(Base):
    __tablename__ = 'programming_languages'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='programming_languages_pkey'),
        UniqueConstraint('label', name='programming_languages_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)

    projects: Mapped['Projects'] = relationship('Projects', secondary='project_language', back_populates='programming_languages')


class Subdomains(Base):
    __tablename__ = 'subdomains'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='subdomains_pkey'),
        UniqueConstraint('label', name='subdomains_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)

    projects: Mapped['Projects'] = relationship('Projects', secondary='project_subdomain', back_populates='subdomains')


class Tags(Base):
    __tablename__ = 'tags'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='tags_pkey'),
        UniqueConstraint('label', name='tags_label_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    label = mapped_column(Text, nullable=False)

    projects: Mapped['Projects'] = relationship('Projects', secondary='project_tag', back_populates='tags')


class Traductions(Base):
    __tablename__ = 'traductions'
    __table_args__ = (
        PrimaryKeyConstraint('label', name='traductions_pkey'),
    )

    label = mapped_column(Text)
    ar = mapped_column(Text)
    fr = mapped_column(Text)
    en = mapped_column(Text)


class Projects(Base):
    __tablename__ = 'projects'
    __table_args__ = (
        ForeignKeyConstraint(['id_domain'], ['domains.id'], name='projects_id_domain_fkey'),
        PrimaryKeyConstraint('id', name='projects_pkey'),
        UniqueConstraint('github_link', name='projects_github_link_key'),
        UniqueConstraint('name', name='projects_name_key'),
        UniqueConstraint('production_link', name='projects_production_link_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    name = mapped_column(Text, nullable=False)
    description = mapped_column(Text)
    github_link = mapped_column(Text)
    production_link = mapped_column(Text)
    realization_date = mapped_column(Date)
    image = mapped_column(Text)
    id_domain = mapped_column(Uuid)

    frameworks: Mapped['Frameworks'] = relationship('Frameworks', secondary='project_framework', back_populates='projects')
    keywords: Mapped['Keywords'] = relationship('Keywords', secondary='project_keyword', back_populates='projects')
    programming_languages: Mapped['ProgrammingLanguages'] = relationship('ProgrammingLanguages', secondary='project_language', back_populates='projects')
    domains: Mapped[Optional['Domains']] = relationship('Domains', back_populates='projects')
    subdomains: Mapped['Subdomains'] = relationship('Subdomains', secondary='project_subdomain', back_populates='projects')
    tags: Mapped['Tags'] = relationship('Tags', secondary='project_tag', back_populates='projects')


class Skills(Base):
    __tablename__ = 'skills'
    __table_args__ = (
        ForeignKeyConstraint(['category_id'], ['categories.id'], name='skills_category_id_fkey'),
        PrimaryKeyConstraint('id', name='skills_pkey'),
        UniqueConstraint('skill', name='skills_skill_key')
    )

    id = mapped_column(Uuid, server_default=text('gen_random_uuid()'))
    skill = mapped_column(Text, nullable=False)
    category_id = mapped_column(Uuid)

    category: Mapped[Optional['Categories']] = relationship('Categories', back_populates='skills')


t_project_framework = Table(
    'project_framework', metadata,
    Column('id_project', Uuid, nullable=False),
    Column('id_framework', Uuid, nullable=False),
    ForeignKeyConstraint(['id_framework'], ['frameworks.id'], name='project_framework_id_framework_fkey'),
    ForeignKeyConstraint(['id_project'], ['projects.id'], name='project_framework_id_project_fkey'),
    PrimaryKeyConstraint('id_project', 'id_framework', name='project_framework_pkey')
)


t_project_keyword = Table(
    'project_keyword', metadata,
    Column('id_project', Uuid, nullable=False),
    Column('id_keyword', Uuid, nullable=False),
    ForeignKeyConstraint(['id_keyword'], ['keywords.id'], name='project_keyword_id_keyword_fkey'),
    ForeignKeyConstraint(['id_project'], ['projects.id'], name='project_keyword_id_project_fkey'),
    PrimaryKeyConstraint('id_project', 'id_keyword', name='project_keyword_pkey')
)


t_project_language = Table(
    'project_language', metadata,
    Column('id_project', Uuid, nullable=False),
    Column('id_programming_language', Uuid, nullable=False),
    ForeignKeyConstraint(['id_programming_language'], ['programming_languages.id'], name='project_language_id_programming_language_fkey'),
    ForeignKeyConstraint(['id_project'], ['projects.id'], name='project_language_id_project_fkey'),
    PrimaryKeyConstraint('id_project', 'id_programming_language', name='project_language_pkey')
)


t_project_subdomain = Table(
    'project_subdomain', metadata,
    Column('id_project', Uuid, nullable=False),
    Column('id_subdomain', Uuid, nullable=False),
    ForeignKeyConstraint(['id_project'], ['projects.id'], name='project_subdomain_id_project_fkey'),
    ForeignKeyConstraint(['id_subdomain'], ['subdomains.id'], name='project_subdomain_id_subdomain_fkey'),
    PrimaryKeyConstraint('id_project', 'id_subdomain', name='project_subdomain_pkey')
)


t_project_tag = Table(
    'project_tag', metadata,
    Column('id_project', Uuid, nullable=False),
    Column('id_tag', Uuid, nullable=False),
    ForeignKeyConstraint(['id_project'], ['projects.id'], name='project_tag_id_project_fkey'),
    ForeignKeyConstraint(['id_tag'], ['tags.id'], name='project_tag_id_tag_fkey'),
    PrimaryKeyConstraint('id_project', 'id_tag', name='project_tag_pkey')
)
