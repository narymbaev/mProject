from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class CommentBase(BaseModel):
    content: str

class CommentCreate(CommentBase):
    pass

class Comment(CommentBase):
    id: int
    post_id: int
    created_at: datetime

    class Config:
        orm_mode = True