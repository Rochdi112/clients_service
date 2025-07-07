from pydantic import BaseModel
from typing import List, Optional

class SiteBase(BaseModel):
    nom: str
    adresse: str

class SiteCreate(SiteBase):
    client_id: int

class SiteRead(SiteBase):
    id: int
    client_id: int

    class Config:
        orm_mode = True

class ClientBase(BaseModel):
    nom: str
    email: str
    telephone: str

class ClientCreate(ClientBase):
    pass

class ClientRead(ClientBase):
    id: int
    sites: List[SiteRead] = []

    class Config:
        orm_mode = True
