# app/schemas.py

from pydantic import BaseModel

class NoteBase(BaseModel):
    title: str
    content: str | None = None  # Optional content

class NoteCreate(NoteBase):
    pass

class NoteOut(NoteBase):
    id: int

    class Config:
        orm_mode = True
