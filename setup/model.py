from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Boolean

Base = declarative_base()

class User(Base):
    __tablename__ = 'notes'
    id =  Column(Integer, primary_key=True)
    owner =  Column(String(50), nullable=False)
    content =  Column(String(150), nullable=False)
    created_date =  Column(Date, nullable=False)
    important =  Column(Boolean, nullable=False)


