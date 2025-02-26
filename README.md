Hospital Management System (HMS)

Project Overview

The Hospital Management System (HMS) is designed to efficiently manage hospital operations, focusing on patient records, doctor appointments, medical records, and billing while ensuring secure and structured data management using Python and MySQL.

Features & Functions

1. Patient Management

add_patient() - Add a new patient.

view_patients() - View all patient records.

update_patient() - Update patient details.

delete_patient() - Delete a patient record.

search_patient() - Search for a specific patient.

2. Doctor Management

add_doctor() - Register a new doctor.

view_doctors() - List all doctors.

update_doctor() - Update doctor information.

delete_doctor() - Remove a doctor from the system.

search_doctor() - Find a doctor by ID.

3. Appointment Management

add_appointment() - Book a new appointment.

view_appointments() - Display all scheduled appointments.

update_appointment() - Modify appointment details.

delete_appointment() - Cancel an appointment.

search_appointment() - Search for an appointment by ID.

4. Medical Records Management

add_medrecord() - Add a medical record for a patient.

view_medrecords() - Retrieve and display medical records.

update_medrecord() - Update a patient's medical history.

delete_medrecord() - Remove a medical record from the system.

search_medrecord() - Search for a medical record by ID.

5. Billing & Invoice Management

add_bill() - Create a new billing entry.

view_bills() - View all billing transactions.

update_bill() - Update billing details.

delete_bill() - Remove a billing record.

search_bill() - Find a billing record by ID.

Tech Stack

Backend: Python

Database: MySQL

Libraries Used: Pandas, NumPy, Matplotlib (for data handling and visualization)

Installation & Setup

Clone the Repository

git clone https://github.com/your-repo/hospital-management-system.git

Install Dependencies

pip install mysql-connector-python pandas numpy matplotlib

Setup MySQL Database

Create a database in MySQL.

Import the provided SQL schema.

Configure database connection in Python.

Run the Project

python main.py

Database Schema

Patients: patient_id, name, age, gender, contact, address

Doctors: doctor_id, name, specialization, contact

Appointments: appointment_id, patient_id, doctor_id, date_time, status

Medical Records: record_id, patient_id, diagnosis, prescription, date

Billing: billing_id, patient_id, amount, status, date

Future Enhancements

GUI implementation using Tkinter or Flask Web Interface.

Advanced analytics dashboard for hospital performance tracking.

Role-based access control for better security.

Contributor

Your Name (MCom Graduate, Aspiring Business Analyst, Data Science Enthusiast)

Contact

For queries, feel free to reach out at [your-email@example.com].
