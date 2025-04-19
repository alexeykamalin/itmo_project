from fastapi import APIRouter, HTTPException, status, Depends
from database.database import get_session
from models.prediction import Prediction
from services.crud import prediction as PredictionService
from services.crud import user as UserService
from typing import List, Dict
import logging

# Configure logging
logger = logging.getLogger(__name__)

prediction_route = APIRouter()

@prediction_route.post(
    '/add_prediction',
    response_model=Dict[str, str],
    status_code=status.HTTP_201_CREATED,
    summary="",
    description="")
async def add_prediction(data: Prediction, user_id: int, session=Depends(get_session)) -> Dict[str, str]:
    """
    """
    try:
        prediction = Prediction(
            result=data.result,
            user_id=user_id,
        )
        PredictionService.create_prediction(Prediction, session)
        logger.info(f"New transaction: {user_id}, {data.result}")
        return {"message": "New prediction complite"}

    except Exception as e:
        logger.error(f"Error during add_tranaction: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error during add_tranaction"
        )

@prediction_route.get(
    "/get_all_predictions_by_user_id",
    response_model=List[Prediction],
    summary="",
    response_description=""
)
async def get_all_predictions_by_user_id(user_id: int, session=Depends(get_session)) -> List[Prediction]:
    """l
    """
    try:
        user = UserService.get_user_by_id(user_id, session)
        predictions = PredictionService.get_all_predictions_by_user_id(user_id, session)
        logger.info(f"Retrieved {user}: {predictions}")
        return predictions
    except Exception as e:
        logger.error(f"Error retrieving users: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Error retrieving usetransactionsrs"
        )