# Logique métier pour Client
from models.client_model import Client
from sqlmodel import Session, select

# Exemple de service

def get_clients(session: Session):
    return session.exec(select(Client)).all()

def get_client(session: Session, client_id: int):
    return session.get(Client, client_id)

def create_client(session: Session, client_data):
    client = Client(**client_data.dict())
    session.add(client)
    session.commit()
    session.refresh(client)
    return client

def update_client(session: Session, client_id: int, client_data):
    client = session.get(Client, client_id)
    if not client:
        return None
    for key, value in client_data.dict(exclude_unset=True).items():
        setattr(client, key, value)
    session.commit()
    session.refresh(client)
    return client

def delete_client(session: Session, client_id: int):
    client = session.get(Client, client_id)
    if not client:
        return None
    session.delete(client)
    session.commit()
    return client

def get_all_clients(db):
    from models.client_model import Client
    return db.exec(select(Client)).all()

def get_client_by_id(db, id: int):
    from models.client_model import Client
    return db.get(Client, id)

def create_client(db, client):
    from models.client_model import Client
    db_client = Client(**client.dict())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def update_client(db, id: int, client_update):
    from models.client_model import Client
    db_client = db.get(Client, id)
    if not db_client:
        return None
    for key, value in client_update.dict(exclude_unset=True).items():
        setattr(db_client, key, value)
    db.commit()
    db.refresh(db_client)
    return db_client

def delete_client(db, id: int):
    from models.client_model import Client
    db_client = db.get(Client, id)
    if not db_client:
        return None
    db.delete(db_client)
    db.commit()
    return db_client
