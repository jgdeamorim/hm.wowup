from database.connection import engine, Base

def create_tables():
    Base.metadata.create_all(bind=engine)
