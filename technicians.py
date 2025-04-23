import sqlite3

class TechnicianManagement:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def create_technician_profile(self, first_name, last_name, contact_info, qualifications, department_id, specialties):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Technicians (first_name, last_name, contact_information, qualifications, department_id, specialties)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, contact_info, qualifications, department_id, specialties))
        conn.commit()
        conn.close()

    def assign_shift(self, technician_id, shift_schedule):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Technicians
        SET shift_schedule = ?
        WHERE technician_id = ?
        """, (shift_schedule, technician_id))
        conn.commit()
        conn.close()

    def log_equipment_usage(self, equipment_id, technician_id, usage_details):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO EquipmentUsage (equipment_id, technician_id, usage_details, usage_date)
        VALUES (?, ?, ?, ?)
        """, (equipment_id, technician_id, usage_details, self._get_current_date()))
        conn.commit()
        conn.close()

    def create_equipment(self, equipment_name, equipment_type, last_maintenance_date, next_maintenance_due_date, assigned_technician_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Equipment (equipment_name, equipment_type, last_maintenance_date, next_maintenance_due_date, assigned_technician_id)
        VALUES (?, ?, ?, ?, ?)
        """, (equipment_name, equipment_type, last_maintenance_date, next_maintenance_due_date, assigned_technician_id))
        conn.commit()
        conn.close()

    def update_equipment_status(self, equipment_id, status):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Equipment
        SET status = ?
        WHERE equipment_id = ?
        """, (status, equipment_id))
        conn.commit()
        conn.close()

    def document_test(self, technician_id, patient_id, test_description, test_results):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO TestResults (technician_id, patient_id, test_description, test_results, test_date)
        VALUES (?, ?, ?, ?, ?)
        """, (technician_id, patient_id, test_description, test_results, self._get_current_date()))
        conn.commit()
        conn.close()

    def _get_current_date(self):
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d')
