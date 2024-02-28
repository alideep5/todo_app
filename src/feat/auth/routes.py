from fastapi import APIRouter

router = APIRouter()

@router.get("/login")
async def read_feature1():
    return {"message": "This is Login API"}