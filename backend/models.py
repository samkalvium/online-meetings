from sqlalchemy import Column, Integer, String
from .database import Base

class Meeting(Base):
    __tablename__ = "meetings"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    host = Column(String, nullable=False)
    scheduled_time = Column(String, nullable=False)
