from fastapi import FastAPI
from .database import engine, Base
from .routes import sweets

app = FastAPI(title="Sweet Shop Backend")

# create tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Sweet Shop Backend Running"}

# register routes
app.include_router(sweets.router)
