# Routes API pour Client
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from database import get_session
from schemas.client_schema import ClientCreate, ClientRead, ClientUpdate
from services.client_service import (
    get_all_clients, get_client_by_id, create_client, update_client, delete_client
)
from dependencies import get_current_user

router = APIRouter(prefix="/clients", tags=["clients"])

@router.get("/", response_model=list[ClientRead])
def list_clients(db: Session = Depends(get_session), user=Depends(get_current_user)):
    return get_all_clients(db)

@router.post("/", response_model=ClientRead)
def create_new_client(client: ClientCreate, db: Session = Depends(get_session), user=Depends(get_current_user)):
    return create_client(db, client)

@router.get("/{id}", response_model=ClientRead)
def get_client(id: int, db: Session = Depends(get_session), user=Depends(get_current_user)):
    client = get_client_by_id(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.put("/{id}", response_model=ClientRead)
def update_client_route(id: int, client_update: ClientUpdate, db: Session = Depends(get_session), user=Depends(get_current_user)):
    client = update_client(db, id, client_update)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{id}")
def delete_client_route(id: int, db: Session = Depends(get_session), user=Depends(get_current_user)):
    client = delete_client(db, id)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"ok": True}
