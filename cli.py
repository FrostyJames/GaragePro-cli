from crud import (
    create_customer, update_customer, delete_customer,
    create_vehicle, update_vehicle, delete_vehicle,
    log_service, view_all_data
)

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
            print("Goodbye! Thank you for using GaragePro.")
            break
        else:
            print(" Invalid option.")

def customer_menu():
    while True:
        print("\n👤 Customer Management")
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
            print(" Customer added.")
        elif choice == "2":
            cid = int(input("Customer ID: "))
            name = input("New name: ") or None
            phone = input("New phone: ") or None
            email = input("New email: ") or None
            address = input("New address: ") or None
            update_customer(cid, name, phone, email, address)
            print("Customer updated.")
        elif choice == "3":
            cid = int(input("Customer ID to delete: "))
            delete_customer(cid)
            print("Customer deleted.")
        elif choice == "4":
            break

def vehicle_menu():
    while True:
        print("\nVehicle Management")
        print("1. Add Vehicle")
        print("2. Update Vehicle")
        print("3. Delete Vehicle")
        print("4. Back")

        choice = input("Choose: ")
        if choice == "1":
            make = input("Make: ")
            model = input("Model: ")
            year = int(input("Year: "))
            customer_id = int(input("Customer ID: "))
            create_vehicle(make, model, year, customer_id)
            print(" Vehicle added.")
        elif choice == "2":
            vid = int(input("Vehicle ID: "))
            make = input("New make: ") or None
            model = input("New model: ") or None
            year = input("New year: ")
            year = int(year) if year else None
            update_vehicle(vid, make, model, year)
            print(" Vehicle updated.")
        elif choice == "3":
            vid = int(input("Vehicle ID to delete: "))
            delete_vehicle(vid)
            print(" Vehicle deleted.")
        elif choice == "4":
            break

def service_menu():
    while True:
        print("\n Service Records")
        print("1. Log Service")
        print("2. Back")

        choice = input("Choose: ")
        if choice == "1":
            vehicle_id = int(input("Vehicle ID: "))
            service_type = input("Service Type: ")
            notes = input("Notes: ")
            cost = float(input("Cost: "))
            log_service(service_type, notes, cost, vehicle_id)
            print("Service logged.")
        elif choice == "2":
            break

if __name__ == "__main__":
    main_menu()