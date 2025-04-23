import sqlite3

class SupportStaffManagement:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def create_staff_profile(self, first_name, last_name, contact_info, job_title, department_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO SupportStaff (first_name, last_name, contact_information, job_title, department_id)
        VALUES (?, ?, ?, ?, ?)
        """, (first_name, last_name, contact_info, job_title, department_id))
        conn.commit()
        conn.close()

    def assign_shift(self, staff_id, shift_schedule):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE SupportStaff
        SET shift_schedule = ?
        WHERE staff_id = ?
        """, (shift_schedule, staff_id))
        conn.commit()
        conn.close()

    def create_task(self, staff_id, task_description, due_date):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Tasks (staff_id, task_description, assigned_date, due_date, status)
        VALUES (?, ?, ?, ?, ?)
        """, (staff_id, task_description, self._get_current_date(), due_date, 'pending'))
        conn.commit()
        conn.close()

    def update_task_status(self, task_id, status):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Tasks
        SET status = ?
        WHERE task_id = ?
        """, (status, task_id))
        conn.commit()
        conn.close()

    def get_staff_tasks(self, staff_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM Tasks
        WHERE staff_id = ?
        """, (staff_id,))
        return cursor.fetchall()

    def _get_current_date(self):
        from datetime import datetime
        return datetime.now().strftime('%Y-%m-%d')
    
    def add_support_staff(self, name, contact_info, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO support_staff (name, contact_info, role)
        VALUES (?, ?, ?)
        """, (name, contact_info, role))
        conn.commit()
        conn.close()

    def view_support_staff(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        SELECT * FROM support_staff
        """)
        staff_records = cursor.fetchall()
        conn.close()
        return staff_records
