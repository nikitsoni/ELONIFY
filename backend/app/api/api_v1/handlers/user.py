from fastapi import APIRouter

user_router = APIRouter()

@user_router.get('test')
async def greet():
    return {"message": "Test User Working"}