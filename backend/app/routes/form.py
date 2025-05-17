from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import crud, schemas
from typing import List
from app import models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/forms", response_model=schemas.FormOut)
def create_form(form: schemas.FormCreate, db: Session = Depends(get_db)):
    return crud.create_form(db, form)

@router.get("/forms", response_model=List[schemas.FormOut])
def list_forms(db: Session = Depends(get_db)):
    return db.query(models.Form).all()

@router.get("/forms/{form_id}/questions")
def get_form_questions(form_id: int, db: Session = Depends(get_db)):
    return db.query(models.Question).filter(models.Question.form_id == form_id).all()


