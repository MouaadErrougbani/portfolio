from sqlalchemy.orm import Session 

from app.models import Traduction
from app.repositories import BaseRepository

class TraductionRepository(BaseRepository[Traduction]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Traduction)
    