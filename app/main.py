from fastapi import FastAPI, HTTPException, Query
from app.db import test_connection, get_postulaciones, get_postulaciones_stats

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

@app.get("/postulaciones-demo")
def postulaciones_demo(limit: int = Query(default=20, ge=1, le=100)):
    try:
        data = get_postulaciones(limit=limit)
        return {
            "status": "ok",
            "count": len(data),
            "limit": limit,
            "data": data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/postulaciones-demo/stats")
def postulaciones_demo_stats():
    try:
        stats = get_postulaciones_stats()
        return {
            "status": "ok",
            "stats": stats
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
