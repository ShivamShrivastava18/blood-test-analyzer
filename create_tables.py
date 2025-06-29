# create_tables.py
from database import engine, metadata
from models import results

metadata.create_all(bind=engine)
