from fastapi import APIRouter, Depends, HTTPException
from peewee import DoesNotExist

from applications.models import ApplicationCreate, ApplicationGet
from organizations.models import OrganizationGet
from auth.models import UserGet
from vacancies.models import VacancyGet
from db.models.user import User
from db.models.vacancy import Vacancy
from db.models.resume import Resume
from db.models.organization import Organization
from db.models.application import Application

from auth.depends import get_user


router = APIRouter()


def get_status(status: int) -> str:
    return [
        "ожидание",
        "принято",
        "отказ",
    ][status]


@router.post("/")
def create(
        vac_slug: str,
        app: ApplicationCreate,
        user: User = Depends(get_user)
) -> ApplicationGet:
    vacancy_db = Vacancy\
        .select(Vacancy, Organization)\
        .join(Organization)\
        .where(Vacancy.slug == vac_slug)\
        .get()

    try:
        Application\
            .get(Application.vacancy == vacancy_db and Application.user == user)
        raise HTTPException(
            403, detail="Can't send multiple applications to one vacancy"
        )
    except DoesNotExist:
        pass

    resume_db = Resume.get(Resume.slug == app.resume_slug)

    Application(
        user=user,
        vacancy=vacancy_db,
        resume=resume_db,
        message=app.message,
        status=0,
    ).save()

    vacancy = vacancy_db.__data__
    vacancy['organization'] = OrganizationGet(
        **vacancy_db.organization.__data__
    )

    return ApplicationGet(
        user=UserGet(**user.__data__),
        vacancy=VacancyGet(**vacancy),
        resume_slug=app.resume_slug,
        message=app.message,
        status=get_status(0)
    )


@router.get("/")
def get(vac_slug: str, user=Depends(get_user)):
    try:
        app_db = Application\
            .select(Application, Vacancy, Organization)\
            .join(Vacancy, on=(Application.vacancy == Vacancy.id))\
            .join(Organization)\
            .join(Resume, on=(Application.resume == Resume.id))\
            .where(User.id == user and Vacancy.slug == vac_slug)\
            .get()
    except DoesNotExist:
        raise HTTPException()

    vacancy = app_db.vacancy.__data__
    vacancy['organization'] = OrganizationGet(
        **app_db.vacancy.organization.__data__
    )

    return ApplicationGet(
        user=UserGet(**user.__data__),
        vacancy=VacancyGet(**vacancy),
        resume_slug=app_db.resume.slug,
        message=app_db.message,
        status=get_status(app_db.status)
    )
