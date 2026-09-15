from database import connect_db


def add_customer():
    name = input("Enter customer name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers (name, phone, email)
        VALUES (?, ?, ?)
    """, (name, phone, email))

    conn.commit()
    conn.close()

    print("\nCustomer added successfully!")


def view_customers():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()

    conn.close()

    if not customers:
        print("\nNo customers found.")
        return

    print("\n--- Customer List ---")

    for customer in customers:
        print(
            f"ID: {customer[0]} | "
            f"Name: {customer[1]} | "
            f"Phone: {customer[2]} | "
            f"Email: {customer[3]}"
        )