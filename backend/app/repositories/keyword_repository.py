from sqlalchemy.orm import Session 

from app.models import Keyword
from app.repositories import BaseRepository

class KeywordRepository(BaseRepository[Keyword]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Keyword)
    