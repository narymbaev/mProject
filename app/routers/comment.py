from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/posts", tags=["users"])

@router.post("/posts/{post_id}/comments/", response_model=schemas.Comment)
def create_comment(post_id: int, comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db_comment = models.Comment(**comment.dict(), post_id=post_id)
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

@router.get("/posts/{post_id}/comments/", response_model=List[schemas.Comment])
def read_comments(post_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    comments = db.query(models.Comment).filter(models.Comment.post_id == post_id).offset(skip).limit(limit).all()
    return comments