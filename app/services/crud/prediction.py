from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from models.prediction import Prediction

def get_all_predictions_by_user_id(user_id: int, session: Session) -> List['Prediction']:
    """
    """
    try:
        statement = select(Prediction).where(Prediction.user_id == user_id)
        predictions = session.exec(statement).all()
        return predictions
    except Exception as e:
        raise

def get_prediction_by_id(prediction_id: int, session: Session) -> Optional['Prediction']:
    """
    """
    try:
        statement = select(Prediction).where(Prediction.id == prediction_id)
        prediction = session.exec(statement).first()
        return prediction
    except Exception as e:
        raise


def create_prediction(prediction: Prediction, session: Session) -> Prediction:
    """
    """
    try:
        session.add(prediction)
        session.commit()
        session.refresh(prediction)
        return prediction
    except Exception as e:
        session.rollback()
        raise

def updateprediction(prediction: Prediction, user_id: int, session: Session) -> Prediction:
    """
    """
    try:
        new_prediction = session.exec(select(Prediction).where(Prediction.user_id == user_id)).one()
        new_prediction.status = prediction.status
        session.commit()
        return prediction
    except Exception as e:
        session.rollback()
        raise