from pydantic import BaseModel, Field


class OrganizationCreate(BaseModel):
    title: str = Field(min_length=3, max_length=255)
    description: str


class OrganizationGet(OrganizationCreate):
    slug: str
