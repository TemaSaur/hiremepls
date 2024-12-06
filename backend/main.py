from fastapi import FastAPI
from auth.routes import router as auth_router


app = FastAPI()


@app.get("/")
def index():
    return "hello world"


app.include_router(auth_router, prefix="/auth")


if __name__ == "__main__":
    from models.create import create_tables

    create_tables()
