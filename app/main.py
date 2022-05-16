from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models

from .routers import user


description = """
Bruno  Dev Test FastapiAppTemplate

## Users

You will be able to:

* **Create users**
* **Read users**
* **Update users**
* **Delete users**
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
        "Docs 1": "http://127.0.0.1:8000/docs",
        "Docs 2": "http://127.0.0.1:8000/redoc"
    }
