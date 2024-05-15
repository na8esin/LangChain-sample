from sqlmodel import create_engine

from app.utils import mysql_uri

engine = create_engine(mysql_uri(), echo=True)