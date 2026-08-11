from sqlalchemy.orm import Session 

from app.models import Subdomain
from app.repositories import BaseRepository

class SubdomainRepository(BaseRepository[Subdomain]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Subdomain)
    