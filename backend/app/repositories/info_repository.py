from sqlalchemy.orm import Session 

from app.models import Info
from app.repositories import BaseRepository

class InfoRepository(BaseRepository[Info]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Info)
    