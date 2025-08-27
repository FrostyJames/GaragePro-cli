from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from datetime import date

Base = declarative_base()
engine = create_engine("sqlite:///garagepro.db")
SessionLocal = sessionmaker(bind=engine)


class Customer(Base):
    __tablename__ = "customers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    vehicles = relationship("Vehicle", back_populates="customer")


class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="vehicles")
    services = relationship("ServiceRecord", back_populates="vehicle")


class ServiceRecord(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True)
    service_type = Column(String)
    notes = Column(String)
    cost = Column(Float)
    date = Column(Date, default=date.today)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    vehicle = relationship("Vehicle", back_populates="services")


Base.metadata.create_all(engine)



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
        if name:
            customer.name = name
        if phone:
            customer.phone = phone
        if email:
            customer.email = email
        if address:
            customer.address = address
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
    vehicle = Vehicle(make=make, model=model, year=year,
                      customer_id=customer_id)
    session.add(vehicle)
    session.commit()
    session.close()
    return vehicle


def update_vehicle(vid, make=None, model=None, year=None):
    session = SessionLocal()
    vehicle = session.get(Vehicle, vid)
    if vehicle:
        if make:
            vehicle.make = make
        if model:
            vehicle.model = model
        if year:
            vehicle.year = year
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
        print(f"\n👤 {c.name} (ID: {c.id})")
        for v in c.vehicles:
            print(f" {v.make} {v.model} ({v.year}) - Vehicle ID: {v.id}")
            for s in v.services:
                print(f"{s.date} - {s.service_type} - KES {s.cost} - {s.notes}")
    session.close()
