from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index() -> dict:
    return {
        "message": "Hello World",
        "mess": "pf",
    }


def home() -> None:
    pass
