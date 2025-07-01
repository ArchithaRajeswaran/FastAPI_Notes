# app/crud.py

from sqlalchemy.orm import Session
from . import models, schemas

# 🔹 Create a new note
def create_note(db: Session, note: schemas.NoteCreate):
    db_note = models.Note(title=note.title, content=note.content)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note

# 🔹 Get all notes
def get_notes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Note).offset(skip).limit(limit).all()

# 🔹 Get a single note by ID
def get_note(db: Session, note_id: int):
    return db.query(models.Note).filter(models.Note.id == note_id).first()

# 🔹 Update a note by ID
def update_note(db: Session, note_id: int, note: schemas.NoteCreate):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note:
        db_note.title = note.title
        db_note.content = note.content
        db.commit()
        db.refresh(db_note)
    return db_note

# 🔹 Delete a note by ID
def delete_note(db: Session, note_id: int):
    db_note = db.query(models.Note).filter(models.Note.id == note_id).first()
    if db_note:
        db.delete(db_note)
        db.commit()
    return db_note

