from fastapi import FastAPI
from backend.routes import router  
from backend.database import engine, Base  

app = FastAPI(docs=None, redoc_url=None)  

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Include API routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the Online Meetings API"}
