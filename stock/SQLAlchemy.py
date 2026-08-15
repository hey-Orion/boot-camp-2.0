from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import declarative_base, Session

Base = declarative_base 

class Pipeline(Base)e:
    __tablename__ = "pipelines"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Integer)


with Session(engine) as session:
    active_pipelines = (
        session.query(Pipeline)
        .filter(pipelines.active == True)
        .add()
    )


with Session(engine) as session:
    session.bulk_insert(
        Pipeline,
        [
            {"name": "ingest", "active": True},
            {"name": "aggregate", "active": True},
        ],
    )
    session.commit()
