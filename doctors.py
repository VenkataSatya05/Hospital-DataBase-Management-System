import sqlite3

class Doctor:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

        
    def view_doctors(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT doctor_id, name, specialization, contact_info, availability_schedule, qualifications, department_id 
        FROM doctors
        """)
        doctors = cursor.fetchall()
        conn.close()
        return doctors

    def accept_appointment(self, appointment_id):
        self.update_appointment(appointment_id, status='Confirmed')

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

    def view_appointments(self, doctor_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Appointments
        WHERE doctor_id = ?
        """, (doctor_id,))
        appointments = cursor.fetchall()
        conn.close()
        return appointments

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

        query += ", ".join(updates) + " WHERE appointment_id = ?"
        params.append(appointment_id)

        cursor.execute(query, params)
        conn.commit()
        conn.close()

    def assign_shift_to_nurse(self, nurse_id, shift_schedule):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Nurses
        SET shift_schedule = ?
        WHERE nurse_id = ?
        """, (shift_schedule, nurse_id))
        conn.commit()
        conn.close()

    def assign_patient_to_nurse(self, nurse_id, patient_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO NursePatients (nurse_id, patient_id)
        VALUES (?, ?)
        """, (nurse_id, patient_id))
        conn.commit()
        conn.close()
