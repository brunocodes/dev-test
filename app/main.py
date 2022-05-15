from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings


# models.Base.metadata.create_all(bind=engine)


description = """
Bruno  Dev Test FastapiAppTemplate

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
* **Update users** (_not implemented_).
* **Delete users** (_not implemented_).
"""

app = FastAPI(
    title="Bruno  Dev Test",
    description=description,
    version="0.0.1"
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user.router)

@app.get("/", include_in_schema=False)
def root():
    return {
        "Docs 1": "api.MySite.com/docs",
        "Docs 2": "api.MySite.com/redoc"
    }
