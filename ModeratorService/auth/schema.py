from pydantic import BaseModel, EmailStr, UUID4, Field, validator, field_validator
from uuid import UUID
from datetime import datetime
from typing import Optional, List, Literal, TypeVar, Generic, Dict

from pydantic.generics import GenericModel


class RegisteredUserCreate(BaseModel):
    user_name: str
    email: EmailStr
    password: str  # Plain password input

    class Config:
        from_attributes = True


class RegisteredUserResponse(BaseModel):
    id: UUID
    user_name: str

    class Config:
        from_attributes = True


class LoginRequest(BaseModel):
    username: str
    password: str


class JWTTokenPayload(BaseModel):
    user_id: UUID
    username: str
    exp: datetime


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: UUID
    name: str
