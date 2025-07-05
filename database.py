# Connexion à la base de données
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///clients.db"
engine = create_engine(DATABASE_URL, echo=True)

# Pour migrations, etc.
def init_db():
    SQLModel.metadata.create_all(engine)

# Dépendance session

def get_session():
    with Session(engine) as session:
        yield session
