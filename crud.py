from datetime import date
from database import SessionLocal
from models import Customer, Vehicle, ServiceRecord

def create_customer(name, phone, email, address):
    session = SessionLocal()
    customer = Customer(name=name, phone=phone, email=email, address=address)
    session.add(customer)
    session.commit()
    session.close()
    return customer

def update_customer(cid, name=None, phone=None, email=None, address=None):
    session = SessionLocal()
    customer = session.get(Customer, cid)
    if customer:
        if name: customer.name = name
        if phone: customer.phone = phone
        if email: customer.email = email
        if address: customer.address = address
        session.commit()
    session.close()

def delete_customer(cid):
    session = SessionLocal()
    customer = session.get(Customer, cid)
    if customer:
        session.delete(customer)
        session.commit()
    session.close()

def create_vehicle(make, model, year, customer_id):
    session = SessionLocal()
    vehicle = Vehicle(make=make, model=model, year=year, customer_id=customer_id)
    session.add(vehicle)
    session.commit()
    session.close()
    return vehicle

def update_vehicle(vid, make=None, model=None, year=None):
    session = SessionLocal()
    vehicle = session.get(Vehicle, vid)
    if vehicle:
        if make: vehicle.make = make
        if model: vehicle.model = model
        if year: vehicle.year = year
        session.commit()
    session.close()

def delete_vehicle(vid):
    session = SessionLocal()
    vehicle = session.get(Vehicle, vid)
    if vehicle:
        session.delete(vehicle)
        session.commit()
    session.close()

def log_service(service_type, notes, cost, vehicle_id, service_date=None):
    session = SessionLocal()
    record = ServiceRecord(
        service_type=service_type,
        notes=notes,
        cost=cost,
        vehicle_id=vehicle_id,
        date=service_date or date.today()
    )
    session.add(record)
    session.commit()
    session.close()
    return record

def view_all_data():
    session = SessionLocal()
    customers = session.query(Customer).all()
    for c in customers:
        print(f"\n{c.name} (ID: {c.id})")
        if not c.vehicles:
            print("  No vehicles registered.")
        for v in c.vehicles:
            print(f"  {v.make} {v.model} ({v.year}) - Vehicle ID: {v.id}")
            if not v.service_records:
                print("    No service records.")
            for s in v.service_records:
                print(f"    {s.date} - {s.service_type} - KES {s.cost} - {s.notes}")
    session.close()

def search_vehicles(make=None, model=None, year=None):
    session = SessionLocal()
    query = session.query(Vehicle).join(Customer)
    if make: query = query.filter(Vehicle.make.ilike(f"%{make}%"))
    if model: query = query.filter(Vehicle.model.ilike(f"%{model}%"))
    if year: query = query.filter(Vehicle.year == year)
    results = query.all()
    session.close()
    return results