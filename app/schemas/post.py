from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .comment import Comment
from dataclasses import dataclass, field

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    created_at: datetime
    comments: List[Comment] = field(default_factory=list)

    class Config:
        orm_mode = True