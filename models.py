from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    profile_picture_url = Column(String, nullable=True)  # New field

# Define your engine if needed
engine = create_engine("postgresql://admin:password@localhost/mydatabase")

