from fastapi import APIRouter, HTTPException
from organizations.models import OrganizationCreate, OrganizationGet
from models.organization import Organization


router = APIRouter()


@router.post("/")
def create(org: OrganizationCreate) -> OrganizationGet:
    org_db = Organization(**org.__dict__)
    org_db.save()
    return OrganizationGet(**org_db.__data__)


@router.get("/")
def get_all() -> list[OrganizationGet]:
    return [OrganizationGet(**x.__data__) for x in Organization.select()]


@router.get("/{slug}")
def get_by_slug(slug: str) -> OrganizationGet:
    print(slug)
    print([(o.slug, o.slug == slug) for o in Organization.select()])
    try:
        return OrganizationGet(**Organization.get(Organization.slug == slug).__data__)
    except Exception:
        raise HTTPException(400, detail="No such organization")
