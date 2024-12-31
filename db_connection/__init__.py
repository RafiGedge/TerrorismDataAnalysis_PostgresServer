from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from settings.postgres_config import DATABASE_URL
from db_connection.models import *

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)
