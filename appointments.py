import sqlite3

class Appointment:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def schedule_appointment(self, patient_id, doctor_id, appointment_datetime, status='Pending', notes=''):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Appointments (patient_id, doctor_id, appointment_datetime, status, notes)
        VALUES (?, ?, ?, ?, ?)
        """, (patient_id, doctor_id, appointment_datetime, status, notes))
        conn.commit()
        conn.close()

    def view_appointments_by_patient(self, patient_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Appointments
        WHERE patient_id = ?
        """, (patient_id,))
        return cursor.fetchall()

    def view_appointments_by_doctor(self, doctor_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Appointments
        WHERE doctor_id = ?
        """, (doctor_id,))
        return cursor.fetchall()

    def update_appointment(self, appointment_id, appointment_datetime=None, status=None, notes=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = "UPDATE Appointments SET "
        updates = []
        params = []

        if appointment_datetime:
            updates.append("appointment_datetime = ?")
            params.append(appointment_datetime)
        if status:
            updates.append("status = ?")
            params.append(status)
        if notes:
            updates.append("notes = ?")
            params.append(notes)

        if updates:
            query += ", ".join(updates) + " WHERE appointment_id = ?"
            params.append(appointment_id)
            cursor.execute(query, params)
            conn.commit()

        else :
            print("No updates provided.")
        conn.close()

    def cancel_appointment(self, appointment_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Appointments
        SET status = 'Cancelled'
        WHERE appointment_id = ?
        """, (appointment_id,))
        conn.commit()
        conn.close()

    def search_appointments(self, date=None, time=None, patient_name=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = "SELECT A.*, P.name FROM Appointments A JOIN Patients P ON A.patient_id = P.patient_id WHERE 1=1"
        params = []

        if date:
            query += " AND DATE(appointment_datetime) = ?"
            params.append(date)
        if time:
            query += " AND TIME(appointment_datetime) = ?"
            params.append(time)
        if patient_name:
            query += " AND P.name LIKE ?"
            params.append(f"%{patient_name}%")

        cursor.execute(query, params)
        return cursor.fetchall()

    def appointment_history(self, patient_id=None, doctor_id=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = "SELECT * FROM Appointments WHERE status IN ('Completed', 'Cancelled')"
        params = []

        if patient_id:
            query += " AND patient_id = ?"
            params.append(patient_id)
        if doctor_id:
            query += " AND doctor_id = ?"
            params.append(doctor_id)

        cursor.execute(query, params)
        return cursor.fetchall()

    def notify_appointment(self, appointment_id, notification_type):
        # Placeholder for sending notifications (Email/SMS)
        if notification_type == 'reminder':
            print(f"Reminder sent for appointment ID: {appointment_id}")
        elif notification_type == 'cancellation':
            print(f"Notification sent for cancellation of appointment ID: {appointment_id}")
        else:
            print("Unknown notification type.")
            
    def book_appointment(self, patient_id, doctor_id, appointment_date, notes):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO appointments (patient_id, doctor_id, appointment_date, status)
        VALUES (?, ?, ?, ?)
        """, (patient_id, doctor_id, appointment_date, 'Pending'))  # Assuming the default status is 'Pending'
        conn.commit()
        conn.close()

    def view_appointments(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT appointment_id, patient_id, doctor_id, appointment_date, status, created_date, updated_date
        FROM appointments
        """)
        appointments = cursor.fetchall()
        conn.close()
        return appointments


        

