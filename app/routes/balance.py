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
        balance = Balance(
            value=data.value,
            user_id=user_id,
        )
        BalanceService.create_balance(balance, session)
        logger.info(f"New Balance: {user_id}, {data.value}")
        return {"message": "New balance complite"}

    except Exception as e:
        logger.error(f"Error during add_tranaction: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error during balance"
        )

@balance_route.get(
    '/get_balance_by_user_id',
    response_model=List[Balance],
    status_code=status.HTTP_201_CREATED,
    summary="",
    description="")   
async def get_balance_by_user_id(user_id: int, session=Depends(get_session)) -> Balance:
    """l
    """
    try:
        user = UserService.get_user_by_id(user_id, session)
        balance = BalanceService.get_balance_by_user_id(user_id, session)
        logger.info(f"Retrieved {user}: {balance}")
        return balance
    except Exception as e:
        logger.error(f"Error retrieving users: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving userbalance"
        )

async def update_balance(data: Balance, user_id: int, session=Depends(get_session)) -> Dict[str, str]:
    """
    """
    try:
        balance = Balance(
            value=data.value,
            user_id=user_id,
        )
        BalanceService.update_balance(balance, session)
        logger.info(f"Balance: {user_id}, {data.value}")
        return {"message": "Update balance complite"}

    except Exception as e:
        logger.error(f"Error during add_tranaction: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error during balance"
        )