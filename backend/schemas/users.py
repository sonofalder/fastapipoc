from typing import Optional
from pydantic import BaseModel, EmailStr


# Schemas validate the data, where as models are what Fast API creates
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserRead(BaseModel):
    username: str
    email: EmailStr
    
    class Config():
        # Used to changing the object into a json dictionary, otherwise it tries to return the object
        # Instead of a json string
        orm_mode = True