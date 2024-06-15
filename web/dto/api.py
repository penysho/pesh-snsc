from datetime import datetime

from pydantic import BaseModel


class PostMediaDto(BaseModel):
    type: str
    sns_url: str


class PostDto(BaseModel):
    id: int
    title: str | None
    like_count: int | None
    comments_count: int | None
    caption: str | None
    permalink: str
    posted_at: datetime
    post_media: list[PostMediaDto]
