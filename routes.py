from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import schemas, crud, models
from .dependencies import get_db, get_current_user

router = APIRouter()

@router.get("/clients", response_model=list[schemas.ClientRead])
def read_clients(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.get_clients(db)

@router.post("/clients", response_model=schemas.ClientRead)
def create_client(client: schemas.ClientCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.create_client(db, client)

@router.get("/sites", response_model=list[schemas.SiteRead])
def read_sites(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.get_sites(db)

@router.post("/sites", response_model=schemas.SiteRead)
def create_site(site: schemas.SiteCreate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    return crud.create_site(db, site)
