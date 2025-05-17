from pydantic import BaseModel
from typing import List, Optional

class PatientCreate(BaseModel):
    name: str
    age: int

class PatientOut(BaseModel):
    id: int
    name: str
    age: int
    class Config:
        orm_mode = True

class QuestionCreate(BaseModel):
    text: str

class FormCreate(BaseModel):
    name: str
    questions: List[QuestionCreate]

class FormOut(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True

class SurveyCreate(BaseModel):
    patient_id: int
    form_id: int

class ResponseCreate(BaseModel):
    survey_id: int
    question_id: int
    answer: str
