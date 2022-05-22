from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from requests import post

from . import models
from .database import engine
from .routers import post, user, auth, vote

from .config import settings
#print(settings.dict())

# # create tables in postgres
# # not needed if we use alembic anymore
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    # "https://www.google.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"], # allow GET requests only
    allow_headers=["*"], # allow 
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
async def root():
    return {'message': 'this has changed'}