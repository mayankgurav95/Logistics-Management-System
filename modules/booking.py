from database import connect_db


def create_booking():
    print("\n--- Create New Booking ---")

    customer_id = input("Enter customer ID: ")
    pickup = input("Enter pickup location: ")
    destination = input("Enter destination: ")
    package_type = input("Enter package type: ")
    weight = float(input("Enter package weight (kg): "))
    delivery_type = input("Enter delivery type (Standard/Express): ")

    # Calculate price
    if delivery_type.lower() == "express":
        price = 100 + (weight * 100)
    else:
        price = 50 + (weight * 70)

    conn = connect_db()
    cursor = conn.cursor()

    # Check whether customer exists
    cursor.execute(
        "SELECT * FROM customers WHERE customer_id = ?",
        (customer_id,)
    )

    customer = cursor.fetchone()

    if not customer:
        print("\nCustomer not found!")
        conn.close()
        return

    # Insert booking
    cursor.execute("""
        INSERT INTO bookings
        (customer_id, pickup_location, destination, package_type,
         weight, delivery_type, price)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        customer_id,
        pickup,
        destination,
        package_type,
        weight,
        delivery_type,
        price
    ))

    booking_id = cursor.lastrowid

    conn.commit()
    conn.close()

    print("\nBooking created successfully!")
    print(f"Booking ID: LGS{booking_id:05d}")
    print(f"Price: ₹{price:.2f}")
    print("Status: BOOKED")


def view_bookings():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            bookings.booking_id,
            customers.name,
            bookings.pickup_location,
            bookings.destination,
            bookings.package_type,
            bookings.weight,
            bookings.delivery_type,
            bookings.price,
            bookings.status
        FROM bookings
        JOIN customers
        ON bookings.customer_id = customers.customer_id
    """)

    bookings = cursor.fetchall()

    conn.close()

    if not bookings:
        print("\nNo bookings found.")
        return

    print("\n--- Booking List ---")

    for booking in bookings:
        print(
            f"\nBooking ID: LGS{booking[0]:05d}"
            f"\nCustomer: {booking[1]}"
            f"\nFrom: {booking[2]}"
            f"\nTo: {booking[3]}"
            f"\nPackage: {booking[4]}"
            f"\nWeight: {booking[5]} kg"
            f"\nDelivery Type: {booking[6]}"
            f"\nPrice: ₹{booking[7]:.2f}"
            f"\nStatus: {booking[8]}"
        )