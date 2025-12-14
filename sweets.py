from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Sweet

router = APIRouter(prefix="/api/sweets", tags=["Sweets"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ADD SWEET
@router.post("/")
def add_sweet(sweet: dict, db: Session = Depends(get_db)):
    new_sweet = Sweet(**sweet)
    db.add(new_sweet)
    db.commit()
    db.refresh(new_sweet)
    return new_sweet

# GET ALL SWEETS
@router.get("/")
def get_sweets(db: Session = Depends(get_db)):
    return db.query(Sweet).all()

# PURCHASE SWEET
@router.post("/{sweet_id}/purchase")
def purchase_sweet(sweet_id: int, db: Session = Depends(get_db)):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    if sweet.quantity <= 0:
        raise HTTPException(status_code=400, detail="Out of stock")

    sweet.quantity -= 1
    db.commit()
    return {"message": "Sweet purchased", "remaining": sweet.quantity}

# RESTOCK SWEET
@router.post("/{sweet_id}/restock")
def restock_sweet(sweet_id: int, amount: int, db: Session = Depends(get_db)):
    sweet = db.query(Sweet).filter(Sweet.id == sweet_id).first()
    if not sweet:
        raise HTTPException(status_code=404, detail="Sweet not found")

    sweet.quantity += amount
    db.commit()
    return {"message": "Sweet restocked", "quantity": sweet.quantity}
