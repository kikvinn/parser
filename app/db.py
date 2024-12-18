# app.py
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Schedule(Base):
    __tablename__ = 'schedule'
    
    id = Column(Integer, primary_key=True)
    subject = Column(String)
    date = Column(Date)
    time = Column(String)
    location = Column(String)

# Создаем базу данных
DATABASE_URL = 'sqlite:///db/school_schedule.db'
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def insert_schedule(schedule):
    session = Session()
    for day in schedule:
        for event in day:
            new_event = Schedule(
                date=event['date'],
                time=event['times'],
                subject=event['subject'],
                location=event['location']
            )
            session.add(new_event)
    session.commit()
    session.close()

def get_schedule_for_date(date):
    session = Session()
    events = session.query(Schedule).filter(Schedule.date == date).all()
    session.close()
    return events
