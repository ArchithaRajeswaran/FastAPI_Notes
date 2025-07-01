# app/main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine

# 🔹 Create the FastAPI app
app = FastAPI()

# 🔹 Create DB tables if they don't exist
models.Base.metadata.create_all(bind=engine)

# 🔹 Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ✅ Route: Create a new note
@app.post("/notes/", response_model=schemas.NoteOut)
def create_note(note: schemas.NoteCreate, db: Session = Depends(get_db)):
    return crud.create_note(db=db, note=note)

# ✅ Route: Get all notes
@app.get("/notes/", response_model=list[schemas.NoteOut])
def read_notes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_notes(db, skip=skip, limit=limit)

# ✅ Route: Get a note by ID
@app.get("/notes/{note_id}", response_model=schemas.NoteOut)
def read_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.get_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# ✅ Route: Update a note
@app.put("/notes/{note_id}", response_model=schemas.NoteOut)
def update_note(note_id: int, note: schemas.NoteCreate, db: Session = Depends(get_db)):
    db_note = crud.update_note(db, note_id, note)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return db_note

# ✅ Route: Delete a note
@app.delete("/notes/{note_id}")
def delete_note(note_id: int, db: Session = Depends(get_db)):
    db_note = crud.delete_note(db, note_id)
    if db_note is None:
        raise HTTPException(status_code=404, detail="Note not found")
    return {"message": "Note deleted"}
