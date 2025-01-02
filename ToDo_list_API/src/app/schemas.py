from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class TaskCreate(BaseModel):
    title: str
    description: Optional[str]

class TaskUpdate(BaseModel):
    completed: bool
