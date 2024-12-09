from pydantic import BaseModel, Field
from organizations.models import OrganizationGet


class VacancyCreate(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=32)
    pay: int = Field(ge=0)
    worktime: str


class VacancyGet(VacancyCreate):
    organization: OrganizationGet
    slug: str
