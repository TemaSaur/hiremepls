from fastapi import APIRouter, HTTPException

from vacancies.models import VacancyCreate, VacancyGet
from organizations.models import OrganizationGet

from db.models.vacancy import Vacancy
from db.models.organization import Organization

from peewee import DoesNotExist


router = APIRouter()
org_router = APIRouter()


@org_router.post("/")
def create(org_slug: str, vacancy: VacancyCreate) -> VacancyGet:
    try:
        org_db = Organization.get(Organization.slug == org_slug)
    except DoesNotExist:
        raise HTTPException(400, "No such organization")

    org = OrganizationGet(**org_db.__data__)

    vacancy_db = Vacancy(**vacancy.__dict__, organization=org_db)
    vacancy_db.save()

    res = vacancy_db.__data__
    res['organization'] = org
    return VacancyGet(**res)


@router.get("/")
def get_all() -> list[VacancyGet]:
    vacancies = []
    for vacancy_db in Vacancy.select(Vacancy, Organization).join(Organization):
        org = OrganizationGet(**vacancy_db.organization.__data__)
        vacancy = vacancy_db.__data__
        vacancy["organization"] = org

        vacancies.append(vacancy)
    return vacancies


@org_router.get("/")
def get_org_all(org_slug: str) -> list[VacancyGet]:
    vacancies = []
    for vacancy_db in Vacancy\
            .select(Vacancy, Organization)\
            .join(Organization)\
            .where(Organization.slug == org_slug):
        org = OrganizationGet(**vacancy_db.organization.__data__)
        vacancy = vacancy_db.__data__
        vacancy["organization"] = org

        vacancies.append(vacancy)
    return vacancies


@router.get("/{slug}")
def get_one(slug: str) -> VacancyGet:
    vacancy_db = Vacancy\
        .select(Vacancy, Organization)\
        .join(Organization)\
        .where(Vacancy.slug == slug)\
        .first()
    res = vacancy_db.__data__
    res['organization'] = OrganizationGet(**vacancy_db.organization.__data__)
    return VacancyGet(**res)
