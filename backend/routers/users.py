from fastapi import APIRouter, HTTPException
from database import SessionLocal
import models
import schemas
from passlib.hash import bcrypt

router = APIRouter()

db = SessionLocal()

@router.post("/register")
def register(user: schemas.UserCreate):

    hashed_password = bcrypt.hash(user.password)

    new_user = models.User(
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()

    return {"message": "User registered successfully"}


@router.post("/login")
def login(user: schemas.UserLogin):

    db_user = db.query(models.User).filter(
        models.User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    if not bcrypt.verify(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Incorrect password")

    return {"message": "Login successful"}