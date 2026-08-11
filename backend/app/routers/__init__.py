from .category import router as category_router
from .skill import router as skill_router
from .contact import router as contact_router
from .diploma import router as diploma_router
from .domain import router as domain_router
from .framework import router as framework_router
from .info import router as info_router
from .keyword import router as keyword_router
from .language import router as language_router
from .navigation import router as navigation_router
from .programming_language import router as programming_language_router
from .project import router as project_router
from .subdomain import router as subdomain_router
from .tag import router as tag_router
from .traduction import router as traduction_router

__all__ = [
    "category_router",
    "skill_router",
    "contact_router",
    "diploma_router",
    "domain_router",
    "framework_router",
    "info_router",
    "keyword_router",
    "language_router",
    "navigation_router",
    "programming_language_router",
    "project_router",
    "subdomain_router",
    "tag_router",
    "traduction_router",
]