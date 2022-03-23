from sqlalchemy import create_engine,inspect
from sqlalchemy.orm import sessionmaker
from config import *
from models import *

engine = create_engine(DATABASE_URI,echo=True)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)    

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    