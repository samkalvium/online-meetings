from sqlalchemy import Column, Integer, String
from .database import Base

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    host = Column(String)
    scheduled_time = Column(String)
