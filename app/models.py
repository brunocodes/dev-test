from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

class UserIn(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime