import sqlite3

class EmergencyContactsManagement:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name
        self.create_tables()

    def create_tables(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()

        # Create EmergencyContacts table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS EmergencyContacts (
                contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                contact_name TEXT NOT NULL,
                relationship TEXT NOT NULL,
                phone_number TEXT NOT NULL,
                email_address TEXT,
                address TEXT,
                special_instructions TEXT,
                FOREIGN KEY (patient_id) REFERENCES Patients(patient_id)
            )
        """)

        conn.commit()
        conn.close()

    def create_emergency_contact(self, patient_id, contact_name, relationship, phone_number, email_address=None, address=None, special_instructions=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO EmergencyContacts (patient_id, contact_name, relationship, phone_number, email_address, address, special_instructions)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (patient_id, contact_name, relationship, phone_number, email_address, address, special_instructions))
        conn.commit()
        conn.close()

    def update_emergency_contact(self, contact_id, contact_name, relationship, phone_number, email_address=None, address=None, special_instructions=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE EmergencyContacts
        SET contact_name = ?, relationship = ?, phone_number = ?, email_address = ?, address = ?, special_instructions = ?
        WHERE contact_id = ?
        """, (contact_name, relationship, phone_number, email_address, address, special_instructions, contact_id))
        conn.commit()
        conn.close()

    def notify_emergency_contact(self, contact_id, message):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        # Placeholder for notification logic (e.g., send an email or SMS)
        cursor.execute("""
        SELECT phone_number, email_address FROM EmergencyContacts
        WHERE contact_id = ?
        """, (contact_id,))
        contact_info = cursor.fetchone()
        if contact_info:
            phone_number, email_address = contact_info
            # Implement notification logic here
            print(f"Notify {phone_number} or {email_address}: {message}")
        conn.close()

    def view_emergency_contacts(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM EmergencyContacts")
        contacts = cursor.fetchall()
        conn.close()
        return contacts
    def delete_emergency_contact(self, contact_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM EmergencyContacts WHERE contact_id = ?", (contact_id,))
        conn.commit()
        conn.close()

