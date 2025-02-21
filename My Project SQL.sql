

create database Hospital_Management_System;
use hospital_management_system;


-- Patients Table

CREATE TABLE Patients (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    gender ENUM('Male', 'Female') NOT NULL,
    address VARCHAR(255),
    contact_number VARCHAR(15) UNIQUE NOT NULL,
    medical_history TEXT
);

-- Doctors Table

CREATE TABLE Doctors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    specialization VARCHAR(100) NOT NULL,
    contact_number VARCHAR(15) UNIQUE NOT NULL,
    availability VARCHAR(50) NOT NULL
);

-- Appointments Table
CREATE TABLE Appointments (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    appointment_date DATE NOT NULL,
    status ENUM('Scheduled', 'Completed', 'Cancelled') NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id) ON DELETE CASCADE
);

-- Medical Records Table
CREATE TABLE MedicalRecords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    doctor_id INT NOT NULL,
    diagnosis VARCHAR(255),
    prescription TEXT,
    test_results TEXT,
    FOREIGN KEY (patient_id) REFERENCES Patients(id) ON DELETE CASCADE,
    FOREIGN KEY (doctor_id) REFERENCES Doctors(id) ON DELETE CASCADE
);

-- Billing Table
CREATE TABLE Billing (
    id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT NOT NULL,
    appointment_id INT NOT NULL,
    total_amount DECIMAL(10,2) NOT NULL,
    payment_status ENUM('Paid', 'Pending', 'Failed') NOT NULL,
    FOREIGN KEY (patient_id) REFERENCES Patients(id) ON DELETE CASCADE,
    FOREIGN KEY (appointment_id) REFERENCES Appointments(id) ON DELETE CASCADE
);

select * from doctors;
select * from patients;
select * from appointments;
select * from medicalrecords;
select * from billing;

desc appointments;

select patient_id, P.name, age, gender, medical_history, doctor_id, D.Name, specialization from appointments as A
join patients as P
on P.id = A.id
join doctors as D
on D.id = A.id
where patient_id between 1 and 200;

