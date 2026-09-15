from database import create_tables
from modules.customer import add_customer, view_customers
from modules.booking import create_booking, view_bookings


def show_menu():
    print("\n================================")
    print("   LOGISTICS MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Create Booking")
    print("4. View Bookings")
    print("5. Exit")


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
            print("\nThank you for using Logistics Management System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()