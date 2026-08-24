from sqlalchemy import Column. Integer, String, Boolean, create_engine, text
from sqlalchemy.orm import declarative_base, sessionmaker, Session 

Base = declarative_base()

class pipeline(Base):
    __tablename__ = "pipeline"

    id = Column(Integer, primary_key=True, autoincrement=True) what is this for autoincrement
    name = Column(String(100), nullable=False)
    active = Column(Boolean, default=True)


DB_URL = "postgresql://postgres:postgres@localhost:5432/dataops_db"

engine = create_engine(DB_URL, echo=True) what dose echo true do?

Base.metadata.create_all(engine)
SessionLocal = sessionmaker(bind=engine)


def get_active_pipeline():
    with SessionLocal() as session:
        active_pipeline = session.query(Pipeline).filter(Pipeline.active == True).all()
        return active_pipeline


def insert():
    pipeline_records = [
        {"name": "ETL_Sales_Daily", "active": True},
        {"name": "CDC_User_Events", "active": True},
        {"name": "Legacy_Batch_Sync", "active": False},
    ]

    with SessionLocal() as session:
        session.bulk_insert(Pipeline, pipeline_records)
        session.commit()


def get_pileine(is_active: bool = True):
    with SessionLocal() as session:

        query = text("SELECT id, name, active FROM pipelines WHERE active = :active")
        result = session.execute(query, {'active': is_active})

        rows = result.mappings().all()
        return rows 


