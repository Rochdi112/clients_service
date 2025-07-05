# Schémas Pydantic pour Site
from pydantic import BaseModel
from typing import Optional

class SiteBase(BaseModel):
    name: str
    client_id: int
    address: str

class SiteCreate(BaseModel):
    name: str
    address: str
    client_id: int

class SiteRead(SiteCreate):
    id: int

    class Config:
        orm_mode = True

class SiteUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    client_id: Optional[int] = None
