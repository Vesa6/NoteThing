from fastapi import APIRouter, HTTPException, Depends
from models import Contact
from database import load_contacts, save_contacts
from auth import get_current_user

router = APIRouter()

@router.get("/")
def get_contacts(user: dict = Depends(get_current_user)):
    return load_contacts()

@router.post("/")
def add_contact(contact: Contact, user: dict = Depends(get_current_user)):
    contacts = load_contacts()
    if any(c["id"] == contact.id for c in contacts):
        raise HTTPException(status_code=400, detail="ID already exists")
    contacts.append(contact.dict())
    save_contacts(contacts)
    return {"message": "Contact added successfully"}

#update
@router.put("/{contact_id}")
def update_contact(contact_id: int, contact: Contact, user: dict = Depends(get_current_user)):
    contacts = load_contacts()
    for idx, c in enumerate(contacts):
        if c["id"] == contact_id:
            contacts[idx] = contact.dict()
            save_contacts(contacts)
            return {"message": "Contact updated successfully"}
    raise HTTPException(status_code=404, detail="Contact not found")

@router.delete("/{contact_id}")
def delete_contact(contact_id: int, user: dict = Depends(get_current_user)):
    contacts = load_contacts()
    contacts = [c for c in contacts if c["id"] != contact_id]
    save_contacts(contacts)
    return {"message": "Contact deleted successfully"}

#@router.post("/{users}")
#def add_user()
