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