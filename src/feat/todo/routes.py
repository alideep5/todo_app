from fastapi import APIRouter

router = APIRouter()

@router.get("/todos")
async def read_feature1():
    return {"message": "This is TODO'S API"}