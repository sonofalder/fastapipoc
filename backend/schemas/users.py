from typing import Optional
from pydantic import BaseModel, EmailStr

# Schemas validate the data, where as models are what Fast API creates
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str