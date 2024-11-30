from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from src.Models.User import UserIn, UserOut
from src.database import get_session
from src.services import UserService

router = APIRouter(prefix="/user", tags=["User"])


@router.post("/", response_model=UserOut)
async def create_user(user_dto: UserIn, session: AsyncSession = Depends(get_session)):  # TODO: Написать создание user
    pass
