from sqlalchemy.orm import Session 

from app.models import Framework
from app.repositories import BaseRepository

class FrameworkRepository(BaseRepository[Framework]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Framework)
    