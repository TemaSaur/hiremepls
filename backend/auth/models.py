from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str = Field(min_length=8, max_length=255)
    course: int = Field(ge=1, le=6)


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserGet(BaseModel):
    email: EmailStr
    full_name: str = Field(min_length=8, max_length=255)
    course: int = Field(ge=1, le=6)
