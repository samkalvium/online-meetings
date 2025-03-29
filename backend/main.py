from fastapi import FastAPI
from .database import engine, Base
from .routes import router

app = FastAPI(docs=None, redoc_url=None)


# Create tables
Base.metadata.create_all(bind=engine)

# Include meeting routes
app.include_router(router)

@app.get("/")
def home():
    return {"message": "Welcome to the Online Meetings API"}
