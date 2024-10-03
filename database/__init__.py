from sqlalchemy import create_engine, MetaData
from databases import Database


DATABASE_URL = 'postgresql://user:1234@localhost:5432/library'

database = Database(DATABASE_URL)
metadata = MetaData()

engine = create_engine(DATABASE_URL)