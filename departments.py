import sqlite3

class Department:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def add_department(self, department_name, head_of_department, location, contact_info):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Departments (department_name, head_of_department, location, contact_info)
        VALUES (?, ?, ?, ?)
        """, (department_name, head_of_department, location, contact_info))
        conn.commit()
        conn.close()

    def view_departments(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Departments")
        return cursor.fetchall()

    def update_department(self, department_id, department_name=None, head_of_department=None, location=None, contact_info=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        updates = []
        if department_name:
            updates.append(f"department_name = '{department_name}'")
        if head_of_department:
            updates.append(f"head_of_department = '{head_of_department}'")
        if location:
            updates.append(f"location = '{location}'")
        if contact_info:
            updates.append(f"contact_info = '{contact_info}'")
        
        if updates:
            updates_str = ", ".join(updates)
            cursor.execute(f"""
            UPDATE Departments
            SET {updates_str}
            WHERE department_id = ?
            """, (department_id,))
            conn.commit()
        conn.close()

    def assign_staff(self, staff_id, department_id, role):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO StaffAssignments (staff_id, department_id, role)
        VALUES (?, ?, ?)
        """, (staff_id, department_id, role))
        conn.commit()
        conn.close()

    def view_staff_assignments(self, department_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM StaffAssignments WHERE department_id = ?", (department_id,))
        return cursor.fetchall()

    def add_service(self, department_id, service_name, protocols):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Services (department_id, service_name, protocols)
        VALUES (?, ?, ?)
        """, (department_id, service_name, protocols))
        conn.commit()
        conn.close()

    def view_services(self, department_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Services WHERE department_id = ?", (department_id,))
        return cursor.fetchall()

    def track_resources(self, department_id, resource_name, quantity):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Resources (department_id, resource_name, quantity)
        VALUES (?, ?, ?)
        """, (department_id, resource_name, quantity))
        conn.commit()
        conn.close()

    def generate_report(self):
        # Placeholder for generating departmental performance reports
        pass

    def budget_management(self, department_id, amount):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Departments
        SET budget = budget + ?
        WHERE department_id = ?
        """, (amount, department_id))
        conn.commit()
        conn.close()
