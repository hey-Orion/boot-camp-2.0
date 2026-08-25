from sqlalchemy import String, Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

DB_URL = "postgresql://postgres:postgres@localhost:5432/my_database"

engine = create_engine(DB_URL)

Base.metadata.create_engine(engine)

SessionLocal = sessionmaker(bind=engine)



def create_users(user_name: str, user_email: str):

    with SessionLocal() as session:
        new_user = User(name=user_name, email=user_email)

        session.add(new_user)

        session.commit()

        session.refresh(new_user)

        return new_user



def get_user_by_id(user_id: int):
    with SessionLocal() as session:

        user = session.query(User).filter(User.id == user_id).first()
        return user 

def get_user_by_name(search_name: str):
    with SessionLocal() as session:
        
        users = session.query(User).filter(User.name == search_name).all()
        return users 



def update_user_email(user_id: int, new_email: str):
    with SessionLocal() as session:

        user = session.query(User).filter(User.id == user_id).first()

        if user:
            user.email = new_email

            session.commit()
            return True 

        return False 



def delete_user(user_id: int):
    with SessionLocal() as session:

        user = session.query(User).Filter(User.id == user_id).first()

        if user:
            session.delete(user)

            session.commit()
            return True
        
        return False
