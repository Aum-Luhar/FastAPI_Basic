from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL= 'postgresql://postgres:password123@localhost:5432/demodb'

engine= create_engine(DATABASE_URL)

SessionLoc= sessionmaker(bind=engine,autoflush=False, autocommit=False)

Base= declarative_base()