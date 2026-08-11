from sqlalchemy.orm import Session 

from app.models import Language
from app.repositories import BaseRepository

class LanguageRepository(BaseRepository[Language]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Language)
    