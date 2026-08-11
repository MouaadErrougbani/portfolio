from sqlalchemy.orm import Session 

from app.models import Tag
from app.repositories import BaseRepository

class TagRepository(BaseRepository[Tag]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Tag)
    