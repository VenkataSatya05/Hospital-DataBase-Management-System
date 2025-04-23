import sqlite3
from datetime import datetime

class Manager:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    # Doctor management methods
    def add_doctor(self, name, specialization, contact_info, availability_schedule, qualifications, department_id):
        """Add a new doctor."""
        self.cursor.execute("""
            INSERT INTO Doctors (name, specialization, contact_info, availability_schedule, qualifications, department_id)
            VALUES (?, ?, ?, ?, ?, ?)""",
            (name, specialization, contact_info, availability_schedule, qualifications, department_id))
        self.connection.commit()

    def delete_doctor(self, doctor_id):
        """Delete a doctor profile."""
        self.cursor.execute("DELETE FROM Doctors WHERE doctor_id = ?", (doctor_id,))
        self.connection.commit()

    def list_doctors(self):
        """List all doctors."""
        self.cursor.execute("SELECT * FROM Doctors")
        return self.cursor.fetchall()

    # Pharmacist management methods
    def add_pharmacist(self, first_name, last_name, contact_info, qualifications, specialties):
        """Add a new pharmacist."""
        self.cursor.execute("""
            INSERT INTO Pharmacists (first_name, last_name, contact_info, qualifications, specialties)
            VALUES (?, ?, ?, ?, ?)""", 
            (first_name, last_name, contact_info, qualifications, specialties))
        self.connection.commit()

    def list_pharmacists(self):
        """List all pharmacists."""
        self.cursor.execute("SELECT * FROM Pharmacists")
        return self.cursor.fetchall()

    def update_pharmacist(self, pharmacist_id, first_name=None, last_name=None, contact_info=None, qualifications=None, specialties=None):
        """Update pharmacist details."""
        updates = []
        if first_name:
            updates.append(f"first_name = '{first_name}'")
        if last_name:
            updates.append(f"last_name = '{last_name}'")
        if contact_info:
            updates.append(f"contact_info = '{contact_info}'")
        if qualifications:
            updates.append(f"qualifications = '{qualifications}'")
        if specialties:
            updates.append(f"specialties = '{specialties}'")
        
        if updates:
            updates_str = ", ".join(updates)
            self.cursor.execute(f"""
            UPDATE Pharmacists
            SET {updates_str}
            WHERE pharmacist_id = ?""", (pharmacist_id,))
            self.connection.commit()


    # Nurse management methods  
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
        if department_id is not None:  # Allow for zero or other falsy values
            updates.append("department_id = ?")
            params.append(department_id)

        if updates:
            updates_str = ", ".join(updates)
            params.append(nurse_id)  # Add nurse_id at the end for the WHERE clause
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

    def close(self):
        """Close the database connection."""
        self.connection.close()
