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

from models import Vehicle
from database import SessionLocal

def create_vehicle(make, model, year, customer_id):
    session = SessionLocal()
    vehicle = Vehicle(
        make=make,
        model=model,
        year=year,
        customer_id=customer_id
    )
    session.add(vehicle)
    session.commit()
    return vehicle