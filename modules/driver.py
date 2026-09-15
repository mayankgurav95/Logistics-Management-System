from database import connect_db


def add_driver():
    print("\n--- Add Driver ---")

    name = input("Enter driver name: ")
    phone = input("Enter phone number: ")
    license_number = input("Enter license number: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO drivers
        (name, phone, license_number)
        VALUES (?, ?, ?)
    """, (name, phone, license_number))

    conn.commit()
    conn.close()

    print("\nDriver added successfully!")


def view_drivers():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            driver_id,
            name,
            phone,
            license_number,
            status
        FROM drivers
    """)

    drivers = cursor.fetchall()

    conn.close()

    if not drivers:
        print("\nNo drivers found.")
        return

    print("\n--- Driver List ---")

    for driver in drivers:
        print(
            f"\nDriver ID: {driver[0]}"
            f"\nName: {driver[1]}"
            f"\nPhone: {driver[2]}"
            f"\nLicense Number: {driver[3]}"
            f"\nStatus: {driver[4]}"
        )