from datetime import datetime
from uuid import UUID, uuid4
from beanie import Document, Indexed
from pydantic import Field, EmailStr

class User(Document):
    user_id: UUID = Field(default_factory = uuid4)
    fullname: str
    email: Indexed(EmailStr, unique = True)
    hashed_password: str
    
    class Settings:
        name = 'users'
