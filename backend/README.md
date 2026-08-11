
## sqlacodegen

est une tool pour "Database Reverse Engineering Database Reflection"  utilise pour créer les models daprès les tables exists dans mon database

pip install sqlacodegen-v2
sqlacodegen_v2 'postgresql://portfolio_user:Mouaad20021127!!@localhost:5432/portfolio_db' > app/models/models.py


## Alembic 

est une toot pour géré les structure de data base


pip install alembic
alembic init alembic
````python
from app.db.database import Base

target_metadata = Base.metadata

```
alembic revision --autogenerate -m "Create users table"
alembic revision --autogenerate -m "Initial schema"
alembic upgrade head

alembic stamp head

app/
│
├── models/
│   ├── __init__.py
│   ├── association_tables.py
│   ├── category.py
│   ├── skill.py
│   ├── contact.py
│   ├── diploma.py
│   ├── domain.py
│   ├── framework.py
│   ├── info.py
│   ├── keyword.py
│   ├── language.py
│   ├── navigation.py
│   ├── programming_language.py
│   ├── project.py
│   ├── subdomain.py
│   ├── tag.py
│   └── traduction.py