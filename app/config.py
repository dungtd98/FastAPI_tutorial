from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import URL
# DATABASE_URL = "postgresql://postgres:Dungtd201198@@localhost:5432/python_db"
DATABASE_URL = URL.create('postgresql', 
                          username='postgres', 
                          password="Dungtd201198@", 
                          host='localhost',
                          port=5555, 
                          database='python_db')
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()