from fastapi import APIRouter, HTTPException, status, Depends
from database.database import get_session
from models.user import User
from models.balance import Balance
from services.crud import user as UserService
from services.crud import balance as BalanceService
from typing import List, Dict
import logging

# Configure logging
logger = logging.getLogger(__name__)

balance_route = APIRouter()

@balance_route.post(
    '/add_balance',
    response_model=Dict[str, str],
    status_code=status.HTTP_201_CREATED,
    summary="",
    description="")
async def add_balance(data: Balance, user_id: int, session=Depends(get_session)) -> Dict[str, str]:
    """
    """
    try:
        Balance = Balance(
            value=data.value,
            user_id=user_id,
        )
        BalanceService.create_balance(Balance, session)
        logger.info(f"New Balance: {user_id}, {data.velue}")
        return {"message": "New transaction complite"}

    except Exception as e:
        logger.error(f"Error during add_tranaction: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error during balance"
        )
