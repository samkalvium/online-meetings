from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Meeting
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Define Pydantic model for validation
class MeetingCreate(BaseModel):
    title: str
    description: str
    host: str
    scheduled_time: str

# API to create a meeting
@router.post("/meetings/", response_model=MeetingCreate)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = Meeting(**meeting.dict())
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

# API to get all meetings
@router.get("/meetings/", response_model=List[MeetingCreate])
def get_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).all()
