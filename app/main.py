from fastapi import FastAPI
from app.db import test_connection

app = FastAPI(title="MVP DataOps Docente")

@app.get("/")
def root():
    return {"message": "API MVP DataOps Docente activa"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/db-health")
def db_health():
    return test_connection()
