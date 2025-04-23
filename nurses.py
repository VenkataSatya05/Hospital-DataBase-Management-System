import sqlite3

class Nurse:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def record_patient_care(self, nurse_id, patient_id, activity, timestamp):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO PatientCareActivities (nurse_id, patient_id, activity, timestamp)
        VALUES (?, ?, ?, ?)
        """, (nurse_id, patient_id, activity, timestamp))
        conn.commit()
        conn.close()

    def view_patient_care_activities(self, nurse_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM PatientCareActivities
        WHERE nurse_id = ?
        """, (nurse_id,))
        return cursor.fetchall()

    def add_nurse(self, name, contact_info, qualifications, role, department_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO nurses (name, contact_info, qualifications, role, department_id)
        VALUES (?, ?, ?, ?, ?)
        """, (name, contact_info, qualifications, role, department_id))
        conn.commit()
        conn.close()

    def view_nurses(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Nurses")
        return cursor.fetchall()

    def update_nurse(self, nurse_id, first_name=None, last_name=None, contact_info=None, qualifications=None, department_id=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        updates = []
        params = []

        if first_name:
            updates.append("first_name = ?")
            params.append(first_name)
        if last_name:
            updates.append("last_name = ?")
            params.append(last_name)
        if contact_info:
            updates.append("contact_info = ?")
            params.append(contact_info)
        if qualifications:
            updates.append("qualifications = ?")
            params.append(qualifications)
        if department_id is not None:
            updates.append("department_id = ?")
            params.append(department_id)

        if updates:
            updates_str = ", ".join(updates)
            params.append(nurse_id)  # Add nurse_id for WHERE clause
            cursor.execute(f"""
            UPDATE Nurses
            SET {updates_str}
            WHERE nurse_id = ?
            """, params)
            conn.commit()
        conn.close()

    def delete_nurse(self, nurse_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM nurses WHERE nurse_id = ?", (nurse_id,))
        conn.commit()
        conn.close()
