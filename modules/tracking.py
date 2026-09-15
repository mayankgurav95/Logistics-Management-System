from database import connect_db


VALID_STATUSES = [
    "BOOKED",
    "PICKED_UP",
    "IN_TRANSIT",
    "OUT_FOR_DELIVERY",
    "DELIVERED",
    "CANCELLED"
]


def track_booking():
    print("\n--- Track Shipment ---")

    booking_id = input("Enter booking ID: ")

    # Remove LGS prefix if user enters LGS00001
    if booking_id.upper().startswith("LGS"):
        booking_id = booking_id[3:]

    if not booking_id.isdigit():
        print("\nInvalid booking ID!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            bookings.booking_id,
            customers.name,
            bookings.pickup_location,
            bookings.destination,
            bookings.status
        FROM bookings
        JOIN customers
        ON bookings.customer_id = customers.customer_id
        WHERE bookings.booking_id = ?
    """, (int(booking_id),))

    booking = cursor.fetchone()

    conn.close()

    if not booking:
        print("\nBooking not found!")
        return

    print("\n--- Shipment Details ---")
    print(f"Booking ID: LGS{booking[0]:05d}")
    print(f"Customer: {booking[1]}")
    print(f"From: {booking[2]}")
    print(f"To: {booking[3]}")
    print(f"Status: {booking[4]}")


def update_status():
    print("\n--- Update Shipment Status ---")

    booking_id = input("Enter booking ID: ")

    if booking_id.upper().startswith("LGS"):
        booking_id = booking_id[3:]

    if not booking_id.isdigit():
        print("\nInvalid booking ID!")
        return

    print("\nAvailable statuses:")

    for index, status in enumerate(VALID_STATUSES, start=1):
        print(f"{index}. {status}")

    choice = input("\nSelect new status: ")

    if not choice.isdigit() or not 1 <= int(choice) <= len(VALID_STATUSES):
        print("\nInvalid status selection!")
        return

    new_status = VALID_STATUSES[int(choice) - 1]

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT booking_id FROM bookings WHERE booking_id = ?",
        (int(booking_id),)
    )

    booking = cursor.fetchone()

    if not booking:
        print("\nBooking not found!")
        conn.close()
        return

    cursor.execute("""
        UPDATE bookings
        SET status = ?
        WHERE booking_id = ?
    """, (new_status, int(booking_id)))

    conn.commit()
    conn.close()

    print(f"\nShipment status updated to: {new_status}")