from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date, Text
from sqlalchemy.orm import relationship
from database import Base


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    email = Column(String)
    address = Column(String)
    vehicles = relationship(
        "Vehicle", back_populates="customer", cascade="all, delete")


class Vehicle(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    customer = relationship("Customer", back_populates="vehicles")
    service_records = relationship(
        "ServiceRecord", back_populates="vehicle", cascade="all, delete")


class ServiceRecord(Base):
    __tablename__ = 'service_records'
    id = Column(Integer, primary_key=True)
    service_type = Column(String)
    date = Column(Date)
    notes = Column(Text)
    cost = Column(Float)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    vehicle = relationship("Vehicle", back_populates="service_records")
