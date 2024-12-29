from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import *
from settings.postgres_config import DATABASE_URL

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)

session_maker = sessionmaker(bind=engine)
