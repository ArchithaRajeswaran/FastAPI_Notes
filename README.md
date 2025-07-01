# FastAPI_Notes
FastAPI Notes API stores and manages notes with endpoints to create, read, update, and delete entries using FastAPI for routing, Pydantic for validation, and can connect to a database like PostgreSQL for persistent storage.

Import Statements:

FastAPI: the main class to create your API app.

HTTPException: allows you to send custom error messages, e.g. “Note not found.”

Depends: helps manage dependencies

Session: SQLAlchemy’s DB session object.

models, schemas, crud: these are your Python files where:
1.models.py - defines your DB tables
2.schemas.py →-defines request & response data shapes
3.crud.py → logic for creating, reading, updating, deleting notes

SessionLocal, engine:
1.engine: connects SQLAlchemy to your Postgres database.
2.SessionLocal: a function that creates DB sessions.
________________________________________________________
Create the FastAPI app

You create an instance of FastAPI called app.

This app holds all your routes (endpoints).
_________________________________________________________
 Create tables in Database
 
 SQLAlchemy uses metadata to track your DB tables.

create_all() creates tables in the database if they don’t exist.

bind=engine means “connect this to my Postgres database.”
__________________________________________________________
Dependency to get DB session

creates a database session (db = SessionLocal())

yield db passes the session into your endpoint.

finally: db.close() safely closes the connection afterward.
__________________________________________________________
API Routes (Endpoints)

>Create a New Note
@app.post("/notes/"): listens for POST requests at /notes/.
response_model=schemas.NoteOut: defines the response shape.
db: Session = Depends(get_db): gets a DB session for the request.
Calls crud.create_note(...) which does:
creates a new Note object
saves it in PostgreSQL
returns the saved note

>Get All Notes
@app.get(...): listens for GET requests at /notes/.
Returns a list of notes.
skip and limit:
skip → how many records to skip (for pagination)
limit → max number of records to return

>Updates a note:
ID comes from the URL.
New data comes from JSON body.
If note not found → 404 error.
Otherwise returns the updated note.

>Delete a Note
Deletes the note with the given ID.
