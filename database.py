import sqlite3


def connect_db():
    return sqlite3.connect("logistics.db")


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Customer table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            email TEXT
        )
    """)

    # Booking table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER NOT NULL,
            pickup_location TEXT NOT NULL,
            destination TEXT NOT NULL,
            package_type TEXT NOT NULL,
            weight REAL NOT NULL,
            delivery_type TEXT NOT NULL,
            price REAL NOT NULL,
            status TEXT DEFAULT 'BOOKED',
            FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        )
    """)

    # Vehicle table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
            vehicle_number TEXT NOT NULL UNIQUE,
            vehicle_type TEXT NOT NULL,
            capacity REAL NOT NULL,
            status TEXT DEFAULT 'AVAILABLE'
        )
    """)

    # Driver table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            driver_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            license_number TEXT NOT NULL UNIQUE,
            status TEXT DEFAULT 'AVAILABLE'
        )
    """)

    # Payment table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            booking_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            payment_method TEXT NOT NULL,
            payment_status TEXT DEFAULT 'PAID',
            payment_date TEXT NOT NULL,
            FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
        )
    """)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_tables()
    print("Database and tables created successfully!")