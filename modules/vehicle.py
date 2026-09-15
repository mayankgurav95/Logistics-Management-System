from database import connect_db


def add_vehicle():
    print("\n--- Add Vehicle ---")

    vehicle_number = input("Enter vehicle number: ")
    vehicle_type = input("Enter vehicle type: ")
    capacity = float(input("Enter vehicle capacity (kg): "))

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO vehicles
        (vehicle_number, vehicle_type, capacity)
        VALUES (?, ?, ?)
    """, (vehicle_number, vehicle_type, capacity))

    conn.commit()
    conn.close()

    print("\nVehicle added successfully!")


def view_vehicles():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            vehicle_id,
            vehicle_number,
            vehicle_type,
            capacity,
            status
        FROM vehicles
    """)

    vehicles = cursor.fetchall()

    conn.close()

    if not vehicles:
        print("\nNo vehicles found.")
        return

    print("\n--- Vehicle List ---")

    for vehicle in vehicles:
        print(
            f"\nVehicle ID: {vehicle[0]}"
            f"\nVehicle Number: {vehicle[1]}"
            f"\nVehicle Type: {vehicle[2]}"
            f"\nCapacity: {vehicle[3]} kg"
            f"\nStatus: {vehicle[4]}"
        )