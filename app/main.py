from fastapi import FastAPI
from .routers import user, post, comment
from .database import engine
from .models import user as user_model, post as post_model, comment as comment_model


user_model.Base.metadata.create_all(bind=engine)
post_model.Base.metadata.create_all(bind=engine)
comment_model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Blog Platform API")

app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)