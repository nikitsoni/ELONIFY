from typing import Optional
from uuid import UUID
from pydantic import BaseModel, EmailStr, Field

class UserAuth(BaseModel):
    fullname: str = Field(..., description="user name")
    email: EmailStr = Field(..., description="user email")
    password: str = Field(..., description="user password")
    