from customer_menu import customer_menu
from vehicle_menu import vehicle_menu
from service_menu import service_menu

def main_menu():
    while True:
        print("\n🚗 GaragePro CLI Main Menu")
        print("1. Customer Management")
        print("2. Vehicle Management")
        print("3. Service Records")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            customer_menu()
        elif choice == "2":
            vehicle_menu()
        elif choice == "3":
            service_menu()
        elif choice == "4":
            print("👋 Exiting GaragePro CLI. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main_menu()