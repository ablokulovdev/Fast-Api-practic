from sqlalchemy import URL,create_engine
from sqlalchemy.orm import sessionmaker

from config import core



DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=core.DB_USER,
    password=core.DB_PASS,
    database=core.DB_NAME,
    host=core.DB_HOST,
    port=core.DB_PORT,
)

engine = create_engine(DATABASE_URL)

Localsession = sessionmaker(bind=engine)
