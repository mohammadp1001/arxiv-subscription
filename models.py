from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date

Base = declarative_base()

class data_user(Base):

    __tablename__ = "users"    
    id = Column(Integer,primary_key=True)
    KEYWORDS = Column(String(500),nullable=False)
    EMAIL = Column(String(200),nullable=False)
    CATEGORIES = Column(String(200),nullable=False)
    DATE_CREATED = Column(Date,default=datetime.utcnow)
    
    def __init__(self, KEYWORDS, EMAIL, CATEGORIES):
        self.KEYWORDS = KEYWORDS
        self.EMAIL = EMAIL
        self.CATEGORIES = CATEGORIES
        
        
    def __repr__(self):
        return "<User(email='{}', keywords='{}', categories={}, date_created={})>"\
                .format(self.EMAIL, self.KEYWORDS, self.CATEGORIES, self.DATE_CREATED)
        