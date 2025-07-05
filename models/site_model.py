# SQLModel pour Site
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from .client_model import Client

class Site(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    address: str
    client_id: int = Field(foreign_key="client.id")
    client: "Client" = Relationship(back_populates="sites")
