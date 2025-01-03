from fastapi import FastAPI
from .routers import user # , post, comment
from .database import engine
from . import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog Platform API")

app.include_router(user.router)
# app.include_router(post.router)
# app.include_router(comment.router)