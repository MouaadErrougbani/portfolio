from sqlalchemy.orm import Session 

from app.models import Diploma
from app.repositories import BaseRepository

class DiplomaRepository(BaseRepository[Diploma]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Diploma)
    