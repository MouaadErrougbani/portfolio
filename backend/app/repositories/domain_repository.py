from sqlalchemy.orm import Session 

from app.models import Domain
from app.repositories import BaseRepository

class DomainRepository(BaseRepository[Domain]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Domain)
    