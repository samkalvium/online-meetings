from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .models import Meeting
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Pydantic model for creating a meeting
class MeetingCreate(BaseModel):
    title: str
    description: str
    host: str
    scheduled_time: str

# Pydantic model for response (includes ID)
class MeetingResponse(MeetingCreate):
    id: int

# Route to create a meeting
@router.post("/meetings/", response_model=MeetingResponse)
def create_meeting(meeting: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = Meeting(**meeting.dict())
    db.add(db_meeting)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

# Route to get all meetings
@router.get("/meetings/", response_model=List[MeetingResponse])
def get_meetings(db: Session = Depends(get_db)):
    return db.query(Meeting).all()

# Route to update a meeting
@router.put("/meetings/{meeting_id}/", response_model=MeetingResponse)
def update_meeting(meeting_id: int, updated_data: MeetingCreate, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not db_meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    for key, value in updated_data.dict().items():
        setattr(db_meeting, key, value)
    db.commit()
    db.refresh(db_meeting)
    return db_meeting

# Route to delete a meeting
@router.delete("/meetings/{meeting_id}/")
def delete_meeting(meeting_id: int, db: Session = Depends(get_db)):
    db_meeting = db.query(Meeting).filter(Meeting.id == meeting_id).first()
    if not db_meeting:
        raise HTTPException(status_code=404, detail="Meeting not found")

    db.delete(db_meeting)
    db.commit()
    return {"message": "Meeting deleted successfully"}
