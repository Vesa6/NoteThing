from fastapi import FastAPI
from routes import router as contact_router
from auth import router as auth_router

app = FastAPI()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(contact_router, prefix="/contacts", tags=["contacts"])

@app.get("/")
def read_root():
    return {"message": "Contact Book API is running"}
