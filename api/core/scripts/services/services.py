from fastapi import APIRouter
from core.scripts.handlers.handlers import get_reception_content, get_clinic_content, get_patient_file, get_side_bar

router = APIRouter()

@router.get("/get_reception_content")
def reception_content():
    return get_reception_content()
@router.get("/get_clinic_content")
def clinic_content():
    return get_clinic_content()
@router.get("/get_patient_file")
def patient_file():
    return get_patient_file()
@router.get("/get_side_bar")
def side_bar_content():
    return get_side_bar()