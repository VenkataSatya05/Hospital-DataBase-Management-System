import sqlite3

class MedicationManagement:
    def __init__(self, db_name='hospital.db'):
        self.db_name = db_name

    def create_medication_profile(self, drug_name, dosage_form, strength, indications, manufacturer, expiration_date, quantity_on_hand, reorder_level):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Medications (drug_name, dosage_form, strength, indications, manufacturer, expiration_date, quantity_on_hand, reorder_level)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (drug_name, dosage_form, strength, indications, manufacturer, expiration_date, quantity_on_hand, reorder_level))
        conn.commit()
        conn.close()

    def update_medication_inventory(self, medication_id, quantity_on_hand):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        UPDATE Medications
        SET quantity_on_hand = ?
        WHERE medication_id = ?
        """, (quantity_on_hand, medication_id))
        conn.commit()
        conn.close()

    def create_prescription(self, patient_id, medication_id, dosage, route_of_administration, frequency, start_date, end_date, prescriber_id):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO Prescriptions (patient_id, medication_id, dosage, route_of_administration, frequency, start_date, end_date, prescriber_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (patient_id, medication_id, dosage, route_of_administration, frequency, start_date, end_date, prescriber_id))
        conn.commit()
        conn.close()

    def document_medication_administration(self, prescription_id, administration_time, dosage_administered, administered_by, observations):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO MAR (prescription_id, administration_time, dosage_administered, administered_by, observations)
        VALUES (?, ?, ?, ?, ?)
        """, (prescription_id, administration_time, dosage_administered, administered_by, observations))
        conn.commit()
        conn.close()

    def check_for_interactions(self, medication_id):
        # Placeholder for checking drug interactions
        return "No known interactions"
    
    def view_medications(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Medications")
        medications = cursor.fetchall()
        conn.close()
        return medications

