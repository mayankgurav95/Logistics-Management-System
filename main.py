from database import create_tables
from modules.customer import add_customer, view_customers
from modules.booking import create_booking, view_bookings
from modules.tracking import track_booking, update_status
from modules.vehicle import add_vehicle, view_vehicles
from modules.driver import add_driver, view_drivers


def show_menu():
    print("\n================================")
    print("   LOGISTICS MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Create Booking")
    print("4. View Bookings")
    print("5. Track Shipment")
    print("6. Update Shipment Status")
    print("7. Add Vehicle")
    print("8. View Vehicles")
    print("9. Add Driver")
    print("10. View Drivers")
    print("11. Exit")


def main():
    create_tables()

    while True:
        show_menu()

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_customer()

        elif choice == "2":
            view_customers()

        elif choice == "3":
            create_booking()

        elif choice == "4":
            view_bookings()

        elif choice == "5":
            track_booking()

        elif choice == "6":
            update_status()

        elif choice == "7":
            add_vehicle()

        elif choice == "8":
            view_vehicles()

        elif choice == "9":
            add_driver()

        elif choice == "10":
            view_drivers()

        elif choice == "11":
            print("\nThank you for using Logistics Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()