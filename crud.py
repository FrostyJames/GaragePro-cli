from database import SessionLocal
from models import Customer, Vehicle, ServiceRecord
from datetime import date


def create_customer(name, phone, email, address):
    with SessionLocal() as session:
        customer = Customer(
            name=name,
            phone_number=phone,
            email=email,
            address=address
        )
        session.add(customer)
        session.commit()
        session.refresh(customer)
        return customer

def create_vehicle(make, model, year, customer_id):
    with SessionLocal() as session:
        vehicle = Vehicle(
            make=make,
            model=model,
            year=year,
            customer_id=customer_id
        )
        session.add(vehicle)
        session.commit()
        session.refresh(vehicle)
        return vehicle

def log_service(service_type, notes, cost, vehicle_id, service_date=None):
    with SessionLocal() as session:
        service = ServiceRecord(
            service_type=service_type,
            notes=notes,
            cost=cost,
            vehicle_id=vehicle_id,
            date=service_date or date.today()
        )
        session.add(service)
        session.commit()
        session.refresh(service)
        return service

# ------------------ READ ------------------

def view_service_history(vehicle_id):
    with SessionLocal() as session:
        records = session.query(ServiceRecord).filter_by(vehicle_id=vehicle_id).all()
        return records

# ------------------ UPDATE ------------------

def update_customer(customer_id, name=None, phone=None, email=None, address=None):
    with SessionLocal() as session:
        customer = session.get(Customer, customer_id)
        if not customer:
            return None
        if name: customer.name = name
        if phone: customer.phone_number = phone
        if email: customer.email = email
        if address: customer.address = address
        session.commit()
        session.refresh(customer)
        return customer

def update_vehicle(vehicle_id, make=None, model=None, year=None):
    with SessionLocal() as session:
        vehicle = session.get(Vehicle, vehicle_id)
        if not vehicle:
            return None
        if make: vehicle.make = make
        if model: vehicle.model = model
        if year: vehicle.year = year
        session.commit()
        session.refresh(vehicle)
        return vehicle

def update_service(service_id, service_type=None, notes=None, cost=None, date=None):
    with SessionLocal() as session:
        service = session.get(ServiceRecord, service_id)
        if not service:
            return None
        if service_type: service.service_type = service_type
        if notes: service.notes = notes
        if cost: service.cost = cost
        if date: service.date = date
        session.commit()
        session.refresh(service)
        return service

# ------------------ DELETE ------------------

def delete_customer_by_id(customer_id):
    with SessionLocal() as session:
        customer = session.get(Customer, customer_id)
        if customer:
            session.delete(customer)
            session.commit()
            return True
        return False

def delete_vehicle_by_id(vehicle_id):
    with SessionLocal() as session:
        vehicle = session.get(Vehicle, vehicle_id)
        if vehicle:
            session.delete(vehicle)
            session.commit()
            return True
        return False

def delete_service_by_id(service_id):
    with SessionLocal() as session:
        service = session.get(ServiceRecord, service_id)
        if service:
            session.delete(service)
            session.commit()
            return True
        return False