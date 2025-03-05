from sqlalchemy import Boolean,Column,ForeignKey,Integer,String,BigInteger
from . prac_database import Base


class Alpha(Base):
    __tablename__= 'student'
    id= Column(Integer,primary_key=True,index=True)
    title = Column(String)
    body = Column(String)
    number = Column(BigInteger)


class User(Base):
    __tablename__= 'users'

    id= Column(Integer,primary_key=True,index=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)