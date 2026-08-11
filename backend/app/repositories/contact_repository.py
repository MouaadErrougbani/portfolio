from sqlalchemy.orm import Session 

from app.models import Contact
from app.repositories import BaseRepository

class ContactRepository(BaseRepository[Contact]) : 

    def __init__(self, session: Session) -> None:
        super().__init__(session, Contact)
    