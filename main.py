from manager import Manager
from patients import Patient
from doctors import Doctor
from medications import MedicationManagement
from emergency_contacts import EmergencyContactsManagement
from appointments import Appointment
from nurses import Nurse
from pharmacists import Pharmacist
from billing import Billing
from support_staff import SupportStaffManagement
from technicians import TechnicianManagement
from departments import Department
from datetime import datetime

def authenticate_manager():
    password = input("Enter Manager Password: ")
    if password == "satya": 
        return True
    else:
        print("Invalid password. Access denied.")
        return False
    
def authenticate_doctor():
    password = input("Enter doctor Password: ")
    if password == "doctor": 
        return True
    else:
        print("Invalid password. Access denied.")
        return False
def main():
    
    manager_db = Manager("hospital_db.sqlite")
    patient_db = Patient("hospital_db.sqlite")
    doctor_db = Doctor("hospital_db.sqlite")
    medication_db = MedicationManagement("hospital_db.sqlite")
    emergency_contact_db = EmergencyContactsManagement("hospital_db.sqlite")
    appointment_db = Appointment("hospital_db.sqlite")
    nurse_db = Nurse("hospital_db.sqlite")
    pharmacist_db = Pharmacist("hospital_db.sqlite")
    billing_db = Billing("hospital_db.sqlite")
    support_staff_db = SupportStaffManagement("hospital_db.sqlite")
    technician_db = TechnicianManagement("hospital_db.sqlite")
    department_db = Department("hospital_db.sqlite")

    while True:
        print("\n--- Hospital Database Management System ---")
        print("1. Manager")
        print("2. Patients")
        print("3. Doctors")
        print("4. Medications")
        print("5. Emergency Contacts")
        print("6. Appointments")
        print("7. Nurses")
        print("8. Pharmacists")
        print("9. Billing")
        print("10. Support Staff")
        # print("11. Manage Technicians")
        # print("12. Manage Departments")
        print("0. Exit")

        choice = input("Select an option: ").strip()
        print(f"User selected: {choice}")  

        if choice == "1":
            if authenticate_manager():
            # Manage Doctors
                print("1. Add Doctor")
                print("2. View Doctors")
                print("3. Delete Doctor")
                print("4. Add Pharmacist")
                print("5. View Pharmacists")
                print("6. Update Pharmacist")
                print("7. Add Nurse")
                print("8. View Nurse")
                print("9. Update Nurse")
                print("10. Delete Nurse")
                print("11. Back to Main Menu")
            
                manager_choice = input("Select an option: ")

                if manager_choice == "1":
                    name = input("Enter Doctor Name: ")
                    specialization = input("Enter Specialization: ")
                    contact_info = input("Enter Contact Info: ")
                    availability_schedule = input("Enter Availability Schedule: ")
                    qualifications = input("Enter Qualifications: ")
                    department_id = input("Enter Department ID: ")
                    manager_db.add_doctor(name, specialization, contact_info, availability_schedule, qualifications, department_id)
                    print("Doctor added successfully.")
                elif manager_choice == "2":
                    doctors = manager_db.list_doctors()
                    for doctor in doctors:
                        print(doctor)
                elif manager_choice == "3":
                    doctor_id = input("Enter Doctor ID to delete: ")
                    manager_db.delete_doctor(doctor_id)
                    print("Doctor deleted successfully.")
                elif manager_choice == "4":
                    first_name = input("Enter Pharmacist First Name: ")
                    last_name = input("Enter Pharmacist Last Name: ")
                    contact_info = input("Enter Contact Info: ")
                    qualifications = input("Enter Qualifications: ")
                    specialties = input("Enter Specialties: ")
                    manager_db.add_pharmacist(first_name, last_name, contact_info, qualifications, specialties)
                    print("Pharmacist added successfully.")
                elif manager_choice == "5":
                    pharmacists = manager_db.list_pharmacists()
                    for pharmacist in pharmacists:
                        print(pharmacist)
                elif manager_choice == "6":
        
                    pharmacist_id = input("Enter Pharmacist ID to update: ")
                    first_name = input("Enter First Name (leave blank to skip): ")
                    last_name = input("Enter Last Name (leave blank to skip): ")
                    contact_info = input("Enter Contact Info (leave blank to skip): ")
                    qualifications = input("Enter Qualifications (leave blank to skip): ")
                    specialties = input("Enter Specialties (leave blank to skip): ")
                    manager_db.update_pharmacist(pharmacist_id, first_name, last_name, contact_info, qualifications, specialties)
                    print("Pharmacist updated successfully.")
    
                elif manager_choice == "7":
                    name = input("Enter Nurse Name: ")
                    contact_info = input("Enter Contact Info: ")
                    qualifications = input("Enter Qualifications: ")
                    department_id = input("Enter Department ID: ")
                    role = input("Enter Role: ").strip()
                    nurse_db.add_nurse(name, contact_info, qualifications,role, department_id)
                    print("Nurse added successfully.")

                elif manager_choice == "8":
                    nurses = nurse_db.view_nurses()
                    for nurse in nurses:
                        print(nurse)
                elif manager_choice == "9":   
                    nurse_id = input("Enter Nurse ID to update: ")
                    new_name = input("Enter New Name (leave blank if no change): ")
                    new_contact_info = input("Enter New Contact Info (leave blank if no change): ")
                    new_qualifications = input("Enter New Qualifications (leave blank if no change): ")
                    nurse_db.update_nurse(nurse_id, new_name or None, new_contact_info or None, new_qualifications or None)
                    print("Nurse updated successfully.")

                elif manager_choice == "10":
                    nurse_id = input("Enter Nurse ID to delete: ")
                    nurse_db.delete_nurse(nurse_id)
                    print("Nurse deleted successfully.")

                elif manager_choice == "11":
                    continue
        

        elif choice == "2":
            # Manage Patients
            print("1. View Patients")
            print("2. Book Appointment")
            print("3. Cancel Appointment")
            print("4. Reschedule Appointment")
            print("5. View Appointments")
            print("6. Pay Bill")
            print("7. Exit")
            patient_choice = input("Select an option: ")

            if patient_choice == "2":
                first_name = input("Enter Patient First Name: ")
                last_name = input("Enter Patient Last Name: ")
                age = input("Enter Patient Age: ")
                gender = input("Enter Patient Gender: ")
                contact_info = input("Enter Contact Info: ")
                address = input("Enter Address: ")
                medical_history = input("Enter Medical History: ")
                insurance_details = input("Enter Insurance Details: ")

                patient_id=patient_db.add_patient(first_name, last_name, age, gender, contact_info, address, medical_history, insurance_details)
                doctor_id = input("Enter Doctor ID: ")
                appointment_datetime = input("Enter Appointment Date and Time (YYYY-MM-DD HH:MM): ")
                notes = input("Enter Notes (optional): ")

                patient_db.book_appointment(first_name, last_name, age, gender, contact_info, address, medical_history, insurance_details, doctor_id, appointment_datetime, notes)
                print("Appointment booked and patient added successfully.")
                
            elif patient_choice == "1":
                patients = patient_db.view_patients()
                for patient in patients:
                    print(patient)
            
            elif patient_choice == "3":
                appointment_id = input("Enter Appointment ID to cancel: ")
                patient_db.cancel_appointment(appointment_id)
                print("Appointment cancelled successfully.")
            elif patient_choice == "4":
                appointment_id = input("Enter Appointment ID to reschedule: ")
                new_datetime = input("Enter New Date and Time (YYYY-MM-DD HH:MM): ")
                patient_db.reschedule_appointment(appointment_id, new_datetime)
                print("Appointment rescheduled successfully.")
            elif patient_choice == "5":
                patient_id = input("Enter Patient ID: ")
                appointments = patient_db.view_appointments(patient_id)
                for appointment in appointments:
                    print(appointment)
            elif patient_choice == "6":
                billing_records = billing_db.view_billing_records()
                for record in billing_records:
                    print(f"Billing ID: {record[0]}, Amount Due: {record[2]}, Status: {record[4]}")

                billing_id = input("Enter Billing ID to pay: ")
                payment_amount = input("Enter Payment Amount: ")
                payment_method = input("Enter Payment Method (e.g., credit card, cash): ")
                billing_db.process_payment(billing_id, payment_amount, payment_method)
                print("Payment processed successfully.")
            elif patient_choice == "7":
                continue

        elif choice == "3":
            if authenticate_doctor():
            # Manage Doctors
                print("1. View Doctors")
                print("2. Accept Appointment")
                print("3. Cancel Appointment")
                print("4. View Appointments")
                print("5. Assign Shift to nurse")
                print("6. Assign patient to nurse")
                print("7. View Patient Care Activities(from Nurse)")
                print("8. Back to Main Menu")
                doctor_choice = input("Select an option: ")

                if doctor_choice == "1":
                    doctors = doctor_db.view_doctors()
                    for doctor in doctors:
                        print(doctor)
                
                elif doctor_choice == "2":
                    appointment_id = input("Enter Appointment ID to accept: ")
                    doctor_db.accept_appointment(appointment_id)
                    print("Appointment accepted successfully.")
            
                elif doctor_choice == "3":
                    appointment_id = input("Enter Appointment ID to cancel: ")
                    doctor_db.cancel_appointment(appointment_id)
                    print("Appointment cancelled successfully.")
                elif doctor_choice == "4":
                    doctor_id = input("Enter Doctor ID: ")
                    appointments = doctor_db.view_appointments(doctor_id)
                    for appointment in appointments:
                        print(appointment)
                elif doctor_choice == "5":
                    nurse_id = input("Enter Nurse ID: ")
                    shift_schedule = input("Enter Shift Schedule: ")
                    doctor_db.assign_shift_to_nurse(nurse_id, shift_schedule)
                    print("Shift assigned to nurse successfully.")
                elif doctor_choice == "6":
                    nurse_id = input("Enter Nurse ID: ")
                    patient_id = input("Enter Patient ID: ")
                    doctor_db.assign_patient_to_nurse(nurse_id, patient_id)
                    print("Patient assigned to nurse successfully.")
                elif doctor_choice == "7":
                    nurse_id = input("Enter Nurse ID: ")
                    activities = nurse_db.view_patient_care_activities(nurse_id)
                    for activity in activities:
                        print(activity)
                elif doctor_choice == "8":
                    continue

        elif choice == "4":
            # Manage Medications
            print("1. Add Medication")
            print("2. View Medications")
            print("3. Update Medication")
            print("4. Delete Medication")
            print("5. Document Medication Administration")
            print("6. Check for Medication Interactions")
            print("7. Back to Main Menu")
            medication_choice = input("Select an option: ")

            if medication_choice == "1":
                drug_name = input("Enter Drug Name: ")
                dosage_form = input("Enter Dosage Form: ")
                strength = input("Enter Strength: ")
                indications = input("Enter Indications: ")
                manufacturer = input("Enter Manufacturer: ")
                expiration_date = input("Enter Expiration Date (YYYY-MM-DD): ")
                quantity_on_hand = input("Enter Quantity on Hand: ")
                reorder_level = input("Enter Reorder Level: ")

                medication_db.create_medication_profile(drug_name, dosage_form, strength, indications, manufacturer, expiration_date, quantity_on_hand, reorder_level)
                print("Medication added successfully.")
            elif medication_choice == "2":
                medications = medication_db.view_medications()
                for medication in medications:
                    print(medication)
            elif medication_choice == "3":
                medication_id = input("Enter Medication ID to update: ")
                new_quantity_on_hand = input("Enter New Quantity on Hand: ")
                medication_db.update_medication_inventory(medication_id, new_quantity_on_hand)
                print("Medication inventory updated successfully.")
            elif medication_choice == "4":
                medication_id = input("Enter Medication ID to delete: ")
                medication_db.delete_medication(medication_id)
                print("Medication deleted successfully.")
            elif medication_choice == "5":
                prescription_id = input("Enter Prescription ID: ")
                administration_time = input("Enter Administration Time (YYYY-MM-DD HH:MM): ")
                dosage_administered = input("Enter Dosage Administered: ")
                administered_by = input("Enter Administered By: ")
                observations = input("Enter Observations: ")
                medication_db.document_medication_administration(prescription_id, administration_time, dosage_administered, administered_by, observations)
                print("Medication administration documented successfully.")
            elif medication_choice == "6":
                medication_id = input("Enter Medication ID to check for interactions: ")
                interactions = medication_db.check_for_interactions(medication_id)
                if interactions:
                    print("Potential interactions found:")
                    for interaction in interactions:
                        print(interaction)
                else:
                    print("No interactions found.")
            elif medication_choice == "7":
                continue

        

        elif choice == "5":
            # Manage Emergency Contacts
            print("1. Add Emergency Contact")
            print("2. View Emergency Contacts")
            print("3. Update Emergency Contact")
            print("4. Delete Emergency Contact")
            print("5. Back to Main Menu")
            emergency_contact_choice = input("Select an option: ")

            if emergency_contact_choice == "1":
                patient_id = input("Enter Patient ID: ")
                contact_name = input("Enter Contact Name: ")
                contact_relationship = input("Enter Contact Relationship: ")
                contact_number = input("Enter Contact Number: ")
                emergency_contact_db.create_emergency_contact(patient_id, contact_name, contact_relationship, contact_number)
                print("Emergency contact added successfully.")
            elif emergency_contact_choice == "2":
                contacts = emergency_contact_db.view_emergency_contacts()
                for contact in contacts:
                    print(contact)
            elif emergency_contact_choice == "3":
                contact_id = input("Enter Contact ID to update: ")
                new_contact_name = input("Enter New Contact Name (leave blank if no change): ")
                new_contact_relationship = input("Enter New Relationship (leave blank if no change): ")
                new_contact_number = input("Enter New Contact Number (leave blank if no change): ")
                emergency_contact_db.update_emergency_contact(contact_id, new_contact_name or None, new_contact_relationship or None, new_contact_number or None)
                print("Emergency contact updated successfully.")
            elif emergency_contact_choice == "4":
                contact_id = input("Enter Contact ID to delete: ")
                emergency_contact_db.delete_emergency_contact(contact_id)
                print("Emergency contact deleted successfully.")
            elif emergency_contact_choice == "5":
                continue
        
        elif choice == "6":
            # Manage Appointments
            print("1. Add Appointment")
            print("2. View Appointments")
            print("3. Update Appointment")
            print("4. Cancel Appointment")
            print("5. Back to Main Menu")
            appointment_choice = input("Select an option: ")

            if appointment_choice == "1":
                patient_id = input("Enter Patient ID: ")
                doctor_id = input("Enter Doctor ID: ")
                appointment_time = input("Enter Appointment Time (YYYY-MM-DD HH:MM): ")
                notes = input("Enter Notes (optional): ")
                appointment_db.book_appointment(patient_id, doctor_id, appointment_time, notes)
                print("Appointment added successfully.")
            elif appointment_choice == "2":
                appointments = appointment_db.view_appointments()
                for appointment in appointments:
                    print(appointment)
            elif appointment_choice == "3":
                appointment_id = input("Enter Appointment ID to update: ")
                new_time = input("Enter New Time (leave blank if no change): ")
                appointment_db.update_appointment(appointment_id, new_time or None)
                print("Appointment updated successfully.")
            elif appointment_choice == "4":
                appointment_id = input("Enter Appointment ID to cancel: ")
                appointment_db.cancel_appointment(appointment_id)
                print("Appointment cancelled successfully.")
            elif appointment_choice == "5":
                continue

        elif choice == "7":
            # Manage Nurses
            print("\nManage Nurses")
            print("1. Record Patient Care")
            # print("2. View Patient Care Activities")
            print("2. Back to Main Menu")
            nurse_choice = input("Select an option: ")

            if nurse_choice == "1":
                nurse_id = input("Enter Nurse ID: ")
                patient_id = input("Enter Patient ID: ")
                activity = input("Enter Patient Care Activity: ")
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                nurse_db.record_patient_care(nurse_id, patient_id, activity, timestamp)
                print(f"Patient care activity recorded for Nurse {nurse_id} and Patient {patient_id}.")
            # elif nurse_choice == "2":
            #     nurse_id = input("Enter Nurse ID: ")
            #     activities = nurse_db.view_patient_care_activities(nurse_id)
            #     for activity in activities:
            #         print(activity)
            elif nurse_choice == "2":
                continue

        elif choice == "8":
            # Manage Pharmacists
            print("1. Add Pharmacist")
            print("2. View Pharmacists")
            print("3. Update Pharmacist")
            print("4. Delete Pharmacist")
            print("5. Back to Main Menu")
            pharmacist_choice = input("Select an option: ")

            if pharmacist_choice == "1":
                first_name = input("Enter Pharmacist First Name: ")
                last_name = input("Enter Pharmacist Last Name: ")
                contact_info = input("Enter Contact Info: ")
                qualifications = input("Enter Qualifications: ")
                specialties = input("Enter Specialties: ")
                pharmacist_db.add_pharmacist(first_name, last_name, contact_info, qualifications, specialties)
                print("Pharmacist added successfully.")
            elif pharmacist_choice == "2":
                pharmacists = pharmacist_db.view_pharmacists()
                for pharmacist in pharmacists:
                    print(pharmacist)
            elif pharmacist_choice == "3":
                pharmacist_id = input("Enter Pharmacist ID to update: ")
                new_name = input("Enter New Name (leave blank if no change): ")
                new_contact_info = input("Enter New Contact Info (leave blank if no change): ")
                pharmacist_db.update_pharmacist(pharmacist_id, new_name or None, new_contact_info or None)
                print("Pharmacist updated successfully.")
            elif pharmacist_choice == "4":
                pharmacist_id = input("Enter Pharmacist ID to delete: ")
                pharmacist_db.delete_pharmacist(pharmacist_id)
                print("Pharmacist deleted successfully.")
            elif pharmacist_choice == "5":
                continue

        elif choice == "9":
            # Manage Billing
            print("1. Add Billing Record")
            print("2. View Billing Records")
            print("3. Update Billing Record")
            print("4. Delete Billing Record")
            print("5. Back to Main Menu")
            billing_choice = input("Select an option: ")

            if billing_choice == "1":
                patient_id = input("Enter Patient ID: ")
                amount = input("Enter Amount: ")
                date = input("Enter Billing Date (YYYY-MM-DD): ")
                billing_db.add_billing_record(patient_id, amount, date)
                print("Billing record added successfully.")
            elif billing_choice == "2":
                records = billing_db.view_billing_records()
                for record in records:
                    print(record)
            elif billing_choice == "3":
                billing_id = input("Enter Billing ID to update: ")
                new_amount = input("Enter New Amount (leave blank if no change): ")
                billing_db.update_billing_record(billing_id, new_amount or None)
                print("Billing record updated successfully.")
            elif billing_choice == "4":
                billing_id = input("Enter Billing ID to delete: ")
                billing_db.delete_billing_record(billing_id)
                print("Billing record deleted successfully.")
            elif billing_choice == "5":
                continue

        elif choice == "10":
            # Manage Support Staff
            print("1. Add Support Staff")
            print("2. View Support Staff")
            print("3. Update Support Staff")
            print("4. Delete Support Staff")
            print("5. Back to Main Menu")
            support_staff_choice = input("Select an option: ")

            if support_staff_choice == "1":
                name = input("Enter Support Staff Name: ")
                contact_info = input("Enter Contact Info: ")
                role = input("Enter Role: ")
                support_staff_db.add_support_staff(name, contact_info, role)
                print("Support staff added successfully.")
            elif support_staff_choice == "2":
                staff = support_staff_db.view_support_staff()
                for member in staff:
                    print(member)
            elif support_staff_choice == "3":
                staff_id = input("Enter Support Staff ID to update: ")
                new_name = input("Enter New Name (leave blank if no change): ")
                new_contact_info = input("Enter New Contact Info (leave blank if no change): ")
                new_role = input("Enter New Role (leave blank if no change): ")
                support_staff_db.update_support_staff(staff_id, new_name or None, new_contact_info or None, new_role or None)
                print("Support staff updated successfully.")
            elif support_staff_choice == "4":
                staff_id = input("Enter Support Staff ID to delete: ")
                support_staff_db.delete_support_staff(staff_id)
                print("Support staff deleted successfully.")
            elif support_staff_choice == "5":
                continue

        elif choice == "12":
            # Exit
            print("Exiting the application. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
