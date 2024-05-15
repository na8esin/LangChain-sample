from typing import Optional
from pydantic import BaseModel


class Products(BaseModel):

    id: int
    name: str
    description: Optional[str]
