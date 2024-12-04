from fastapi import FastAPI
from models import migrate


app = FastAPI()


@app.get("/")
def index():
    return "hello world"


if __name__ == "__main__":
    migrate.migrate()
