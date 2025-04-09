from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from typing import Dict
from sqlmodel import Session
from database.database import get_session, init_db, get_database_engine
from database.config import get_settings
from models.user import User
from models.prediction import Prediction
from models.transaction import Transaction
from models.balance import Balance
from services.crud.user import get_all_users, create_user
from services.crud.prediction import create_transaction
from services.crud.transaction import create_prediction
import uvicorn
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Сервисное API",
    description="API для управления событиями",
    version="1.0.0"
)

@app.get("/", response_model=Dict[str, str])
async def index() -> Dict[str, str]:
    """
    Корневой эндпоинт, возвращающий приветственное сообщение с информацией о пользователе.
    
    Returns:
        Dict[str, str]: Приветственное сообщение с информацией о пользователе
    """
    return {"message": f"Hello world! User: 123"}



@app.get("/test")
def test():
    """
    Тестовый роут
    """
    return 'Hello world!'


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    logger.warning(f"HTTPException: {exc.detail} для запроса {request.url}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail}
    )

if __name__ == '__main__':
    settings = get_settings()
    init_db(drop_all=True)
    test_user = User(email='test1@gmail.com', password='Qwerty123!', name='Bob', balance=0)
    test_user1 = User(email='test1@gmail.com', password='Qwerty123!', name='Alice', balance=0)
    test_user2 = User(email='test1@gmail.com', password='Qwerty123!', name='Ann', balance=0)
    tr1 = Transaction(type='replenishment', cost=10, user_id=test_user.id)
    tr2 = Transaction(type='replenishment', cost=20, user_id=test_user.id)
    tr3 = Transaction(type='write_off', cost=5, user_id=test_user.id)
    pr1 = Prediction(result='Lorem ipsum dolor sit amet Aenean commodo ligula eget dolor.', user_id=test_user.id)
    pr2 = Prediction(result='Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor.', user_id=test_user.id)
    pr3 = Prediction(result='Lorem ipsum dolor sit amet, consectetuer adipiscing elit.', user_id=test_user.id)

    engine = get_database_engine()
    with Session(engine) as session:
        create_user(test_user, session)
        create_user(test_user1, session)
        create_user(test_user2, session)
        users = get_all_users(session)
        create_transaction(tr1, session)
        create_transaction(tr2, session)
        create_transaction(tr3, session)
        create_prediction(pr1, session)
        create_prediction(pr2, session)
        create_prediction(pr3, session)
    for user in users:
        print(user)
        for transactions in user.transactions:
            pass
        for prediction in user.predictions:
            pass

    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8080,
        reload=True,
        log_level="debug"
    )