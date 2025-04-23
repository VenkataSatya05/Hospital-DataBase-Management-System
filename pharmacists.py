import sqlite3

class Pharmacist:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def add_medication(self, medication_name, dosage_form, strength, stock_level, expiration_date, prescribing_info):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Medications (medication_name, dosage_form, strength, stock_level, expiration_date, prescribing_info)
        VALUES (?, ?, ?, ?, ?, ?)""",
        (medication_name, dosage_form, strength, stock_level, expiration_date, prescribing_info))
        conn.commit()
        conn.close()

    def view_medications(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medications")
        return cursor.fetchall()

    def dispense_medication(self, patient_id, medication_id, dosage, route, notes):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO DispensedMedications (patient_id, medication_id, dosage, route, notes)
        VALUES (?, ?, ?, ?, ?)""",
        (patient_id, medication_id, dosage, route, notes))
        conn.commit()
        conn.close()

    def document_counseling(self, patient_id, medication_id, counseling_notes):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO CounselingRecords (patient_id, medication_id, counseling_notes)
        VALUES (?, ?, ?)""",
        (patient_id, medication_id, counseling_notes))
        conn.commit()
        conn.close()
