from sqlalchemy import Column. Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Pipeline(Base):
    __tablename__ = "piprlines"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)

