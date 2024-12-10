from pydantic import BaseModel, Field
from auth.models import UserGet
from vacancies.models import VacancyGet


class ApplicationCreate(BaseModel):
    resume_slug: str
    message: str = Field(max_length=1024)


class ApplicationGet(ApplicationCreate):
    user: UserGet
    vacancy: VacancyGet
    status: str
