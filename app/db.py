# app.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Subject(Base):
    __tablename__ = 'subject'
    
    id = Column(Integer, primary_key=True)
    subject_name = Column(String)

    mains = relationship("Main", back_populates="subject")

class Main(Base):
    __tablename__ = 'main'
    
    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey('subject.id'))
    date = Column(Date)
    time = Column(String)
    location = Column(String)

    subject = relationship("Subject", back_populates="mains")

# Создаем базу данных
engine = create_engine('sqlite:///../db/school_schedule.db')
Base.metadata.create_all(engine)

# Создаем сессию
Session = sessionmaker(bind=engine)

def add_subject_and_schedule(subject_name, date, time, location):
    session = Session()
    new_subject = Subject(subject_name=subject_name)
    session.add(new_subject)
    session.commit()

    new_schedule = Main(subject_id=new_subject.id, date=date, time=time, location=location)
    session.add(new_schedule)
    session.commit()
    session.close()

def get_schedule():
    session = Session()
    schedules = session.query(Main).all()
    result = []
    for schedule in schedules:
        result.append({
            "id": schedule.id,
            "subject": schedule.subject.subject_name,
            "date": str(schedule.date),
            "time": str(schedule.time),
            "location": schedule.location
        })
    session.close()
    return result
