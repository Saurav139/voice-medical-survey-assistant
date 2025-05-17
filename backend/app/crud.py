from app import models, schemas
from sqlalchemy.orm import Session

def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(**patient.dict())
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

def create_form(db: Session, form: schemas.FormCreate):
    db_form = models.Form(name=form.name)
    db.add(db_form)
    db.commit()
    for q in form.questions:
        question = models.Question(form_id=db_form.id, text=q.text)
        db.add(question)
    db.commit()
    return db_form

def create_survey(db: Session, survey: schemas.SurveyCreate):
    db_survey = models.Survey(**survey.dict())
    db.add(db_survey)
    db.commit()
    db.refresh(db_survey)
    return db_survey

def add_response(db: Session, response: schemas.ResponseCreate):
    db_response = models.Response(**response.dict())
    db.add(db_response)
    db.commit()
    return db_response
