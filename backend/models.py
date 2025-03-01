from pydantic import BaseModel

class Contact(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    address: str = ""
    notes: str = ""

class User(BaseModel):
    username: str
    password: str
