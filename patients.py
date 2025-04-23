import sqlite3
from datetime import datetime

class Patient:
    def __init__(self, db_name='hospital_db.sqlite'):
        self.db_name = db_name

    # Add patient if they don't exist already
    def add_patient(self, first_name, last_name, age, gender, contact_info, address, medical_history, insurance_details):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Insert patient details and return patient ID
        cursor.execute("""
        INSERT INTO patients (first_name, last_name, age, gender, contact_info, address, medical_history, insurance_details)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, age, gender, contact_info, address, medical_history, insurance_details))
        
        conn.commit()
        patient_id = cursor.lastrowid  # Get the last inserted patient ID
        conn.close()
        
        return patient_id

    # Check if patient exists
    def find_patient(self, first_name, last_name, contact_info):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Query to check if patient exists based on unique attributes (name and contact info)
        cursor.execute("""
        SELECT patient_id FROM patients 
        WHERE first_name = ? AND last_name = ? AND contact_info = ?
        """, (first_name, last_name, contact_info))
        
        result = cursor.fetchone()
        conn.close()

        if result:
            return result[0]  # Return patient_id if found
        return None

    # View all patients
    def view_patients(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM patients")
        patients = cursor.fetchall()
        
        conn.close()
        return patients

    # Book appointment (now automatically adds patient if not found)
    def book_appointment(self, first_name, last_name, age, gender, contact_info, address, medical_history, insurance_details, doctor_id, appointment_date, notes='', status='Pending'):
        # Check if patient exists, if not, add the patient
        patient_id = self.find_patient(first_name, last_name, contact_info)
        if not patient_id:
            print(f"Patient {first_name} {last_name} not found, adding new patient to the database...")
            patient_id = self.add_patient(first_name, last_name, age, gender, contact_info, address, medical_history, insurance_details)
        
        # Now book the appointment
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, status, notes)
        VALUES (?, ?, ?, ?, ?)
        """, (patient_id, doctor_id, appointment_date, status, notes))
        conn.commit()
        conn.close()
        print(f"Appointment booked successfully for patient {first_name} {last_name}.")

    def cancel_appointment(self, appointment_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE appointments
        SET status = 'Cancelled'
        WHERE appointment_id = ?
        """, (appointment_id,))
        conn.commit()
        conn.close()

    def reschedule_appointment(self, appointment_id, new_date):
        self.update_appointment(appointment_id, appointment_date=new_date)

    def update_appointment(self, appointment_id, appointment_date=None, status=None, notes=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = "UPDATE appointments SET "
        updates = []
        params = []

        if appointment_date:
            updates.append("appointment_date = ?")
            params.append(appointment_date)
        if status:
            updates.append("status = ?")
            params.append(status)
        if notes:
            updates.append("notes = ?")
            params.append(notes)

        query += ", ".join(updates) + " WHERE appointment_id = ?"
        params.append(appointment_id)

        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def view_appointments(self, patient_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM appointments
        WHERE patient_id = ?
        """, (patient_id,))
        appointments = cursor.fetchall()
        conn.close()
        return appointments
    
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

    # Helper method to get the current date
    def _get_current_date(self):
        return datetime.now().strftime('%Y-%m-%d')
