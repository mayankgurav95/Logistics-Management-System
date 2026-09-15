from database import connect_db
from datetime import date


def add_payment():
    print("\n--- Add Payment ---")

    booking_id = input("Enter booking ID: ")

    if booking_id.upper().startswith("LGS"):
        booking_id = booking_id[3:]

    if not booking_id.isdigit():
        print("\nInvalid booking ID!")
        return

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT booking_id, price
        FROM bookings
        WHERE booking_id = ?
    """, (int(booking_id),))

    booking = cursor.fetchone()

    if not booking:
        print("\nBooking not found!")
        conn.close()
        return

    print(f"\nBooking Amount: ₹{booking[1]:.2f}")

    amount = float(input("Enter payment amount: "))
    payment_method = input(
        "Enter payment method (Cash/UPI/Card): "
    )

    cursor.execute("""
        INSERT INTO payments
        (booking_id, amount, payment_method, payment_date)
        VALUES (?, ?, ?, ?)
    """, (
        int(booking_id),
        amount,
        payment_method,
        date.today().isoformat()
    ))

    conn.commit()
    conn.close()

    print("\nPayment added successfully!")
    print(f"Payment Amount: ₹{amount:.2f}")
    print("Payment Status: PAID")


def view_payments():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            payments.payment_id,
            payments.booking_id,
            customers.name,
            payments.amount,
            payments.payment_method,
            payments.payment_status,
            payments.payment_date
        FROM payments
        JOIN bookings
        ON payments.booking_id = bookings.booking_id
        JOIN customers
        ON bookings.customer_id = customers.customer_id
    """)

    payments = cursor.fetchall()

    conn.close()

    if not payments:
        print("\nNo payments found.")
        return

    print("\n--- Payment List ---")

    for payment in payments:
        print(
            f"\nPayment ID: {payment[0]}"
            f"\nBooking ID: LGS{payment[1]:05d}"
            f"\nCustomer: {payment[2]}"
            f"\nAmount: ₹{payment[3]:.2f}"
            f"\nPayment Method: {payment[4]}"
            f"\nPayment Status: {payment[5]}"
            f"\nPayment Date: {payment[6]}"
        )