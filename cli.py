from crud import (
    create_customer, update_customer, delete_customer,
    create_vehicle, update_vehicle, delete_vehicle,
    log_service, view_all_data, search_vehicles
)
from datetime import datetime

from database import Base, engine
from models import Customer, Vehicle, ServiceRecord

Base.metadata.create_all(bind=engine)

def main_menu():
    while True:
        print("\nGaragePro CLI Main Menu")
        print("1. View All Records")
        print("2. Customer Management")
        print("3. Vehicle Management")
        print("4. Service Records")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            view_all_data()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            vehicle_menu()
        elif choice == "4":
            service_menu()
        elif choice == "5":
            print("Thank you for using GaragePro.")
            break
        else:
            print("Invalid option. Please try again.")

def customer_menu():
    while True:
        print("\nCustomer Management")
        print("1. Add Customer")
        print("2. Update Customer")
        print("3. Delete Customer")
        print("4. Back")

        choice = input("Choose: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            address = input("Address: ")
            create_customer(name, phone, email, address)
            print("Customer added.")
        elif choice == "2":
            try:
                cid = int(input("Customer ID: "))
                name = input("New name (leave blank to keep current): ") or None
                phone = input("New phone: ") or None
                email = input("New email: ") or None
                address = input("New address: ") or None
                update_customer(cid, name, phone, email, address)
                print("Customer updated.")
            except ValueError:
                print("Invalid ID format.")
        elif choice == "3":
            try:
                cid = int(input("Customer ID to delete: "))
                delete_customer(cid)
                print("Customer deleted.")
            except ValueError:
                print("Invalid ID format.")
        elif choice == "4":
            break
        else:
            print("Invalid option.")

def vehicle_menu():
    while True:
        print("\nVehicle Management")
        print("1. Add Vehicle")
        print("2. Update Vehicle")
        print("3. Delete Vehicle")
        print("4. Search Vehicles")
        print("5. Back")

        choice = input("Choose: ")
        if choice == "1":
            try:
                make = input("Make: ")
                model = input("Model: ")
                year = int(input("Year: "))
                customer_id = int(input("Customer ID: "))
                create_vehicle(make, model, year, customer_id)
                print("Vehicle added.")
            except ValueError:
                print("Invalid input. Year and Customer ID must be numbers.")
        elif choice == "2":
            try:
                vid = int(input("Vehicle ID: "))
                make = input("New make: ") or None
                model = input("New model: ") or None
                year_input = input("New year: ")
                year = int(year_input) if year_input else None
                update_vehicle(vid, make, model, year)
                print("Vehicle updated.")
            except ValueError:
                print("Invalid input.")
        elif choice == "3":
            try:
                vid = int(input("Vehicle ID to delete: "))
                delete_vehicle(vid)
                print("Vehicle deleted.")
            except ValueError:
                print("Invalid ID format.")
        elif choice == "4":
            make = input("Search by make (leave blank to skip): ") or None
            model = input("Search by model (leave blank to skip): ") or None
            year_input = input("Search by year (leave blank to skip): ")
            year = int(year_input) if year_input else None

            vehicles = search_vehicles(make, model, year)
            if not vehicles:
                print("No matching vehicles found.")
            else:
                print("\nMatching Vehicles:")
                for v in vehicles:
                    print(f"- ID: {v.id} | {v.make} {v.model} ({v.year}) | Owner ID: {v.customer_id}")
        elif choice == "5":
            break
        else:
            print("Invalid option.")

def service_menu():
    while True:
        print("\nService Records")
        print("1. Log Service")
        print("2. Back")

        choice = input("Choose: ")
        if choice == "1":
            try:
                vehicle_id = int(input("Vehicle ID: "))
                service_type = input("Service Type: ")
                notes = input("Notes: ")
                cost = float(input("Cost: "))
                log_service(service_type, notes, cost, vehicle_id)
                print("Service logged.")
            except ValueError:
                print("Invalid input. Vehicle ID must be an integer and cost must be a number.")
        elif choice == "2":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()