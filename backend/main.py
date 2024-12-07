from fastapi import FastAPI
from auth.routes import router as auth_router
from organizations.routes import router as org_router


app = FastAPI()


@app.get("/")
def index():
    return "hello world"


app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(org_router, prefix="/organizations", tags=["Organizations"])


if __name__ == "__main__":
    from models.create import create_tables

    create_tables()
