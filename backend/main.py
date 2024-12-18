from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.routes import router as auth_router
from organizations.routes import router as org_router
from vacancies.routes import router as vac_router, org_router as org_vac_router
from resumes.routes import router as res_router
from applications.routes import router as app_router, vac_router as vac_app_router


app = FastAPI()

origins = [
    'http://127.0.0.1',
    'http://localhost:3000'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


@app.get("/")
def index():
    return "hello world"


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(org_router, prefix="/organizations", tags=["Organizations"])
app.include_router(vac_router, prefix="/vacancies", tags=["Vacancies"])
app.include_router(res_router, prefix="/resumes", tags=["Resumes"])
app.include_router(app_router, prefix="/applications", tags=["Applications"])
app.include_router(
    org_vac_router,
    prefix="/organizations/{org_slug}/vacancies",
    tags=["Vacancies"])
app.include_router(
    vac_app_router,
    prefix="/vacancies/{vac_slug}/applications",
    tags=["Applications"])
