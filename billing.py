import sqlite3
from datetime import datetime

class Billing:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name
    
    # Add a billing record
    def add_billing_record(self, patient_id, amount, billing_date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO billing (patient_id, amount, bill_date, status)
        VALUES (?, ?, ?, ?)
        """, (patient_id, amount, billing_date, 'pending'))
        conn.commit()
        conn.close()
    
    # View all billing records
    def view_billing_records(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM billing
        """)
        records = cursor.fetchall()
        conn.close()
        return records

    # Update a billing record (e.g., changing amount)
    def update_billing_record(self, billing_id, new_amount):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE billing
        SET amount = ?, updated_date = CURRENT_TIMESTAMP
        WHERE bill_id = ?
        """, (new_amount, billing_id))
        conn.commit()
        conn.close()

    # Delete a billing record
    def delete_billing_record(self, billing_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        DELETE FROM billing
        WHERE bill_id = ?
        """, (billing_id,))
        conn.commit()
        conn.close()

    # Process payment for a billing record
    def process_payment(self, billing_id, payment_amount, payment_method):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO payments (billing_id, payment_date, payment_amount, payment_method)
        VALUES (?, ?, ?, ?)
        """, (billing_id, self._get_current_date(), payment_amount, payment_method))
        
        # Update the billing status
        cursor.execute("""
        UPDATE billing
        SET status = 'paid'
        WHERE bill_id = ?
        """, (billing_id,))
        conn.commit()
        conn.close()

    # Generate the current date for billing records
    def _get_current_date(self):
        return datetime.now().strftime('%Y-%m-%d')
