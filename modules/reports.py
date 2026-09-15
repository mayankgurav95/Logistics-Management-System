from database import connect_db


def show_reports():
    conn = connect_db()
    cursor = conn.cursor()

    print("\n================================")
    print("       LOGISTICS REPORTS")
    print("================================")

    # Total customers
    cursor.execute("SELECT COUNT(*) FROM customers")
    total_customers = cursor.fetchone()[0]

    # Total bookings
    cursor.execute("SELECT COUNT(*) FROM bookings")
    total_bookings = cursor.fetchone()[0]

    # Delivered bookings
    cursor.execute("""
        SELECT COUNT(*)
        FROM bookings
        WHERE status = 'DELIVERED'
    """)
    delivered_bookings = cursor.fetchone()[0]

    # Pending bookings
    cursor.execute("""
        SELECT COUNT(*)
        FROM bookings
        WHERE status NOT IN ('DELIVERED', 'CANCELLED')
    """)
    pending_bookings = cursor.fetchone()[0]

    # Total booking revenue
    cursor.execute("SELECT COALESCE(SUM(price), 0) FROM bookings")
    total_revenue = cursor.fetchone()[0]

    # Total payments
    cursor.execute("SELECT COALESCE(SUM(amount), 0) FROM payments")
    total_payments = cursor.fetchone()[0]

    # Total vehicles
    cursor.execute("SELECT COUNT(*) FROM vehicles")
    total_vehicles = cursor.fetchone()[0]

    # Total drivers
    cursor.execute("SELECT COUNT(*) FROM drivers")
    total_drivers = cursor.fetchone()[0]

    conn.close()

    print(f"\nTotal Customers      : {total_customers}")
    print(f"Total Bookings       : {total_bookings}")
    print(f"Delivered Bookings   : {delivered_bookings}")
    print(f"Pending Bookings     : {pending_bookings}")
    print(f"Total Revenue        : ₹{total_revenue:.2f}")
    print(f"Total Payments       : ₹{total_payments:.2f}")
    print(f"Total Vehicles       : {total_vehicles}")
    print(f"Total Drivers        : {total_drivers}")

    print("\n================================")