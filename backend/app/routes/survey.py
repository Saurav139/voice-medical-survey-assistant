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

@router.post("/surveys")
def create_survey(survey: schemas.SurveyCreate, db: Session = Depends(get_db)):
    return crud.create_survey(db, survey)

# @router.post("/responses")
# def add_response(response: schemas.ResponseCreate, db: Session = Depends(get_db)):
#     return crud.add_response(db, response)

@router.get("/surveys")
def list_surveys(db: Session = Depends(get_db)):
    return db.query(models.Survey).all()

@router.get("/surveys/{survey_id}/responses")
def get_survey_responses(survey_id: int, db: Session = Depends(get_db)):
    return db.query(models.Response).filter(models.Response.survey_id == survey_id).all()

