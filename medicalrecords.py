import sqlite3
from datetime import datetime

class MedicalRecord:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def add_record(self, patient_id, doctor_id, date_of_visit, medical_history, allergies, current_medications, diagnosis, treatment_plan, notes):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO MedicalRecords (patient_id, doctor_id, date_of_visit, medical_history, allergies, current_medications, diagnosis, treatment_plan, notes, created_date, updated_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (patient_id, doctor_id, date_of_visit, medical_history, allergies, current_medications, diagnosis, treatment_plan, notes, datetime.now(), datetime.now()))
        conn.commit()
        conn.close()

    def view_records(self, patient_id=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        if patient_id:
            cursor.execute("SELECT * FROM MedicalRecords WHERE patient_id = ?", (patient_id,))
        else:
            cursor.execute("SELECT * FROM MedicalRecords")
        return cursor.fetchall()

    def update_record(self, record_id, diagnosis=None, treatment_plan=None, notes=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        updates = []
        params = []

        if diagnosis:
            updates.append("diagnosis = ?")
            params.append(diagnosis)
        if treatment_plan:
            updates.append("treatment_plan = ?")
            params.append(treatment_plan)
        if notes:
            updates.append("notes = ?")
            params.append(notes)

        if updates:
            params.append(record_id)
            query = "UPDATE MedicalRecords SET " + ", ".join(updates) + ", updated_date = ? WHERE record_id = ?"
            params.append(datetime.now())
            cursor.execute(query, params)
            conn.commit()
        conn.close()

    def delete_record(self, record_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM MedicalRecords WHERE record_id = ?", (record_id,))
        conn.commit()
        conn.close()

    def search_records(self, patient_name=None, patient_id=None, date_of_visit=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        query = "SELECT * FROM MedicalRecords WHERE"
        conditions = []
        params = []

        if patient_name:
            conditions.append("patient_id IN (SELECT patient_id FROM Patients WHERE name LIKE ?)")
            params.append('%' + patient_name + '%')
        if patient_id:
            conditions.append("patient_id = ?")
            params.append(patient_id)
        if date_of_visit:
            conditions.append("date_of_visit = ?")
            params.append(date_of_visit)

        if conditions:
            query += " " + " AND ".join(conditions)
            cursor.execute(query, params)
        else:
            query = "SELECT * FROM MedicalRecords"
            cursor.execute(query)

        return cursor.fetchall()

    def add_attachment(self, record_id, attachment_path):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Attachments (record_id, attachment_path)
        VALUES (?, ?)
        """, (record_id, attachment_path))
        conn.commit()
        conn.close()

    def view_attachments(self, record_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Attachments WHERE record_id = ?", (record_id,))
        return cursor.fetchall()
