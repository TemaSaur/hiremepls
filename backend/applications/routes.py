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
vac_router = APIRouter()


def get_status(status: int) -> str:
    return [
        "ожидание",
        "принято",
        "отказ",
    ][status]


@vac_router.post("/")
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

    print(vacancy_db.title)

    try:
        h = Application\
            .get((Application.vacancy == vacancy_db) & (Application.user == user))

        print(h)
        print(h.message, h.vacancy)
        raise HTTPException(
            403, detail="Can't send multiple applications to one vacancy"
        )
    except DoesNotExist:
        pass

    try:
        resume_db = Resume.get(Resume.slug == app.resume_slug)
    except DoesNotExist:
        raise HTTPException(400, "No such resume")

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


@vac_router.get("/")
def get_vac(vac_slug: str, user=Depends(get_user)) -> ApplicationGet:
    return get(user, vac_slug)


@router.get("/")
def get_my(user=Depends(get_user)) -> list[ApplicationGet]:
    return get(user)


def get(user: User, vac_slug: str | None = None):
    vac_predicate = True if vac_slug is None else Vacancy.slug == vac_slug
    try:
        app_db = Application\
            .select(Application, Vacancy, Organization)\
            .join(Vacancy, on=(Application.vacancy == Vacancy.id))\
            .join(Organization)\
            .join(Resume, on=(Application.resume == Resume.id))\
            .where((Application.user == user) & (vac_predicate))
        if vac_slug:
            app_db = app_db.get()
    except DoesNotExist:
        raise HTTPException()

    def get_application(app_db):
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

    if vac_slug:
        return get_application(app_db)
    return [get_application(a) for a in app_db]
