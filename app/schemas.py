from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserOut(BaseModel):
    user_id: int
    nome: str
    email: EmailStr
    telefone: str
    endereco: str
    profissao: str

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    user_id: int
    nome: str
    email: EmailStr
    telefone: str
    endereco: str
    profissao: str
    curriculo: Optional[None] = None

class UserUpdate(BaseModel):
    user_id: int
    nome: str
    email: EmailStr
    telefone: str
    endereco: str
    profissao: str
    curriculo: Optional[None] = None