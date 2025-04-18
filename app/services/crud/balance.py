from sqlmodel import Session, select
from typing import List, Optional
from datetime import datetime
from models.balance import Balance

def create_balance(balance: Balance, session: Session) -> Balance:
    """
    """
    try:
        session.add(balance)
        session.commit()
        session.refresh(balance)
        return balance
    except Exception as e:
        session.rollback()
        raise

def get_balance_by_user_id(user_id: int, session: Session) -> Balance:
    """
    """
    try:
        statement = select(Balance).where(Balance.user_id == user_id)
        balance = session.exec(statement).all()
        return balance
    except Exception as e:
        raise

def update_balance(balance: Balance, user_id: int, session: Session) -> Balance:
    """
    """
    try:
        session.add(balance)
        session.commit()
        session.refresh(balance)
        return balance
    except Exception as e:
        session.rollback()
        raise