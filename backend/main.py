from fastapi import FastAPI
from routes import router as contact_router
from auth import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS (Frontend requests), otherwise this sends a "preflight request - OPTIONS"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods, including OPTIONS
    allow_headers=["*"],  # Allow all headers
)


app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(contact_router, prefix="/contacts", tags=["contacts"])

@app.get("/")
def read_root():
    return {"message": "Contact Book API is running"}
