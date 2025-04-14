from sqlmodel import SQLModel, Session, create_engine 
from contextlib import contextmanager
from .config import get_settings
from models.user import User
from services.crud.user import create_user, get_all_users

def get_database_engine():
    """
    Create and configure the SQLAlchemy engine.
    
    Returns:
        Engine: Configured SQLAlchemy engine
    """
    settings = get_settings()
    
    engine = create_engine(
        url=settings.DATABASE_URL_psycopg,
        echo=settings.DEBUG,
        pool_size=5,
        max_overflow=10,
        pool_pre_ping=True,
        pool_recycle=3600
    )
    return engine

engine = get_database_engine()

def get_session():
    with Session(engine) as session:
        yield session
        
def init_db(drop_all: bool = False) -> None:
    """
    Initialize database schema.
    
    Args:
        drop_all: If True, drops all tables before creation
    
    Raises:
        Exception: Any database-related exception
    """
    try:
        engine = get_database_engine()
        if drop_all:
            SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)
        test_user = User(email='test1@gmail.com', password='Qwerty123!', name='Bob')
        test_user1 = User(email='test1@gmail1.com', password='Qwerty123!', name='Alice', is_admin=True)
        with Session(engine) as session:
            users = get_all_users(session)
            if not test_user in users:
                create_user(test_user, session)
            if not test_user1 in users:
                create_user(test_user1, session)
    except Exception as e:
        raise