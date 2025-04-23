import sqlite3
from datetime import datetime

def create_database(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create Managers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS managers (
            manager_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            role TEXT NOT NULL,
            user_id INTEGER,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create Patients table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS patients (
        patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        age INTEGER NOT NULL,
        contact_info TEXT NOT NULL,
        gender TEXT NOT NULL,
        address TEXT NOT NULL,
        medical_history TEXT,
        insurance_details TEXT,
        created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")



    # Create Doctors table
    cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS doctors (
        doctor_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        specialization TEXT NOT NULL,
        availability_schedule TIME,
        contact_info TEXT NOT NULL,
        qualifications TEXT NOT NULL,
        department_id INTEGER,  -- Foreign key to departments table
        created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (department_id) REFERENCES departments(department_id)  -- Assuming you have a departments table
    )
""")


    # Create Medications table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medications (
        medication_id INTEGER PRIMARY KEY AUTOINCREMENT,
        drug_name TEXT NOT NULL,
        dosage_form TEXT NOT NULL,
        strength TEXT NOT NULL,
        indications TEXT NOT NULL,
        manufacturer TEXT NOT NULL,
        expiration_date DATE NOT NULL,
        quantity_on_hand INTEGER NOT NULL,
        reorder_level INTEGER NOT NULL,
        created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
        updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
    )
""")
# Create MAR (Medication Administration Record) table
    cursor.execute("""
                CREATE TABLE IF NOT EXISTS MAR (
                mar_id INTEGER PRIMARY KEY AUTOINCREMENT,
                prescription_id INTEGER NOT NULL,
                administration_time DATETIME NOT NULL,
                dosage_administered TEXT NOT NULL,
                administered_by TEXT NOT NULL,
                observations TEXT,
                created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                updated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (prescription_id) REFERENCES Prescriptions(prescription_id)
    )
""")

    # Create User Accounts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_accounts (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            role TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create Emergency Contacts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS emergency_contacts (
            contact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            contact_name TEXT NOT NULL,
            relationship TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)

    # Create Appointments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            doctor_id INTEGER NOT NULL,
            appointment_date DATETIME NOT NULL,
            status TEXT NOT NULL,
            notes TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
            FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
        )
    """)

    # Create Nurses table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS nurses (
            nurse_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            qualifications TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            role TEXT NOT NULL,
            department_id INTEGER,
            shift_schedule TEXT,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Create NursePatients table to assign patients to nurses
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS NursePatients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nurse_id INTEGER NOT NULL,
            patient_id INTEGER NOT NULL,
            assignment_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (nurse_id) REFERENCES nurses(nurse_id),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS PatientCareActivities (
            activity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            nurse_id INTEGER NOT NULL,
            patient_id INTEGER NOT NULL,
            activity TEXT NOT NULL,
            timestamp DATETIME NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (nurse_id) REFERENCES nurses(nurse_id),
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)

    # Create Pharmacists table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pharmacists (
            pharmacist_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            qualifications TEXT NOT NULL,
            specialties TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create Billing table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing (
            bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER NOT NULL,
            amount REAL NOT NULL,
            bill_date DATETIME NOT NULL,
            status TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (patient_id) REFERENCES patients(patient_id)
        )
    """)

    # Create Support Staff table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS support_staff (
            staff_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            role TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create Technicians table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS technicians (
            technician_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            contact_info TEXT NOT NULL,
            role TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create Departments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            department_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
            updated_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Create the Payments table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            billing_id INTEGER,
            payment_date TEXT,
            payment_amount REAL,
            payment_method TEXT,
            FOREIGN KEY (billing_id) REFERENCES Billings(billing_id)
        )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    create_database("hospital_db.sqlite")
