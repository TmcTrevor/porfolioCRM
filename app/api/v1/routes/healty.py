from fastapi import APIRouter


router = APIRouter()

@router.get("/{user_id}")
def test(user_id : str):
        return user_id
