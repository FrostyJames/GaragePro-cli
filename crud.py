from database import SessionLocal
from models import Customer

def create_customer(name, phone, email, address):
    session = SessionLocal()
    customer = Customer(
        name=name,
        phone_number=phone,
        email=email,
        address=address
    )
    session.add(customer)
    session.commit()
    return customer