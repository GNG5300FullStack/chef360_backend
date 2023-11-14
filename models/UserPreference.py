from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, DateTime
from dbInstance import db

@dataclass
class UserPreference(db.Model):
    """User Model"""
    __tablename__ = 'USER_PREFERENCE'

    E_MAIL:int = Column(String(50), primary_key=True)
    COOKWARE:str = Column(String(255))
    ALLERGICS:str = Column(String(255))
   

