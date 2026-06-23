from fastapi import APIRouter

router = APIRouter()


@router.get("/", tags=["Home"])
def home():
    return {"message": "Clinica Veterinaria API - Factoria F5"}
