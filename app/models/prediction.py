from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from user import User

@dataclass
class Prediction:
    """
    Класс для представления предсказаний.
    
    Attributes:
        id (int): Уникальный идентификатор предсказания
        result (str): Результат предсказания (пока не очень понимаю, какой будет результат, поэтому пока строка :) )
        user (User): Создатель предсказания
        date (str): Дата предсказания
    """
    id: int
    result: str
    user: User
    date: str

    def __post_init__(self) -> None:
        pass

    def get_prediction_by_id(self, id: int) -> None:
        pass

    def get_all_predictions_by_user(self, user: User) -> None:
        pass

    def add_prediction(self, user: User) -> None:
        pass