# Routes API pour Site
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from schemas.site_schema import SiteCreate, SiteRead, SiteUpdate
from services.site_service import (
    get_all_sites, get_sites_by_client, get_site_by_id, create_site, update_site, delete_site
)
from dependencies import get_current_user

router = APIRouter(prefix="/sites", tags=["sites"])

@router.get("/", response_model=list[SiteRead])
def list_sites(db: Session = Depends(get_session), user=Depends(get_current_user)):
    return get_all_sites(db)

@router.get("/by_client/{client_id}", response_model=list[SiteRead])
def list_sites_by_client(client_id: int, db: Session = Depends(get_session), user=Depends(get_current_user)):
    return get_sites_by_client(db, client_id)

@router.get("/{id}", response_model=SiteRead)
def get_site_route(id: int, db: Session = Depends(get_session), user=Depends(get_current_user)):
    site = get_site_by_id(db, id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.post("/", response_model=SiteRead)
def create_new_site(site: SiteCreate, db: Session = Depends(get_session), user=Depends(get_current_user)):
    return create_site(db, site)

@router.put("/{id}", response_model=SiteRead)
def update_site_route(id: int, site_update: SiteUpdate, db: Session = Depends(get_session), user=Depends(get_current_user)):
    site = update_site(db, id, site_update)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return site

@router.delete("/{id}")
def delete_site_route(id: int, db: Session = Depends(get_session), user=Depends(get_current_user)):
    site = delete_site(db, id)
    if not site:
        raise HTTPException(status_code=404, detail="Site not found")
    return {"ok": True}
