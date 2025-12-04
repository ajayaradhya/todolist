

from typing import Optional
from pydantic import BaseModel


class TodoItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = "No description provided"
    completed: bool = False