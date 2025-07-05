# Logique métier pour Site
from models.site_model import Site
from sqlmodel import Session, select

def get_all_sites(db):
    from models.site_model import Site
    return db.exec(select(Site)).all()

def get_sites_by_client(db, client_id: int):
    from models.site_model import Site
    return db.exec(select(Site).where(Site.client_id == client_id)).all()

def get_site_by_id(db, id: int):
    from models.site_model import Site
    return db.get(Site, id)

def create_site(db, site):
    from models.site_model import Site
    db_site = Site(**site.dict())
    db.add(db_site)
    db.commit()
    db.refresh(db_site)
    return db_site

def update_site(db, id: int, site_update):
    from models.site_model import Site
    db_site = db.get(Site, id)
    if not db_site:
        return None
    for key, value in site_update.dict(exclude_unset=True).items():
        setattr(db_site, key, value)
    db.commit()
    db.refresh(db_site)
    return db_site

def delete_site(db, id: int):
    from models.site_model import Site
    db_site = db.get(Site, id)
    if not db_site:
        return None
    db.delete(db_site)
    db.commit()
    return db_site
