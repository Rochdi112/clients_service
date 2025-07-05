# Schémas Pydantic pour Client
from pydantic import BaseModel
from typing import Optional

class ClientBase(BaseModel):
    name: str
    email: str
    phone: str

class ClientCreate(BaseModel):
    name: str
    email: str
    phone: str

class ClientRead(ClientCreate):
    id: int

    class Config:
        orm_mode = True

class ClientUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
