from sqlalchemy.orm import Session 

from app.models import Navigation
from app.repositories import BaseRepository

class NavigationRepository(BaseRepository[Navigation]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Navigation)
    