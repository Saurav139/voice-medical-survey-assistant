from fastapi import FastAPI
from app.routes import patient, form, survey
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(patient.router)
app.include_router(form.router)
app.include_router(survey.router)
