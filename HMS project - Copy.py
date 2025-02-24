{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "911b569a-61c3-413b-a5f5-9d33cc4e049d",
   "metadata": {},
   "source": [
    "### Connecting to Database of MySQL:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "cb05bdb9-4d3f-4c12-ad37-aca842a416ce",
   "metadata": {},
   "outputs": [],
   "source": [
    "import mysql.connector\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "01c18369-5b3a-4564-9513-6902aa5c0d76",
   "metadata": {},
   "outputs": [],
   "source": [
    "conn = mysql.connector.connect(\n",
    "    host = \"localhost\",\n",
    "    user = \"root\",\n",
    "    password = \"mysql\",\n",
    "    database = \"hospital_management_system\"\n",
    ")\n",
    "cursor = conn.cursor()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e1503987-e0c2-4cc8-93ae-0d397607690c",
   "metadata": {},
   "source": [
    "#### Showing All the Tables in the hospital_management_system:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "486100de-22c2-4fb8-983f-aacd62c890fb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "appointments\n",
      "billing\n",
      "doctors\n",
      "medicalrecords\n",
      "patients\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"show tables\")\n",
    "Table_name = cursor.fetchall()\n",
    "for i in Table_name:\n",
    "    for a in i:\n",
    "        print(a)    ## where a is a random alphabet iterator that shows the particular table name.\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bd887612-be70-4508-9835-8c6100804cf2",
   "metadata": {},
   "source": [
    "#### Patients Table Description :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "44a4ddf6-8779-447e-8cf3-fbe3cbc4c47e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "('patient_id', 'int', 'NO', 'PRI', None, 'auto_increment')\n",
      "('patient_name', 'varchar(60)', 'YES', '', None, '')\n",
      "('age', 'int', 'NO', '', None, '')\n",
      "('gender', \"enum('Male','Female')\", 'NO', '', None, '')\n",
      "('address', 'varchar(255)', 'YES', '', None, '')\n",
      "('contact_number', 'varchar(15)', 'NO', 'UNI', None, '')\n",
      "('medical_history', 'text', 'YES', '', None, '')\n"
     ]
    }
   ],
   "source": [
    "cursor.execute(\"desc patients\")\n",
    "Column_name = cursor.fetchall()\n",
    "for i in Column_name:\n",
    "    print(i)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6d04a274-4416-4920-83a6-160d607c136f",
   "metadata": {},
   "source": [
    "## Retrieving Data of Patients Table as DataFrame :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "e3891e63-7908-4173-971b-1ef47b7b694f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import sqlalchemy\n",
    "engine = sqlalchemy.create_engine(f\"mysql+pymysql://{\"root\"}:{\"mysql\"}@{\"localhost\"}/{\"hospital_management_system\"}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7e4970e-89c4-4056-b7fb-d442cbc629af",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 337,
   "id": "9f3e2f19-ffcf-4e7e-a9ec-c265267f5a20",
   "metadata": {},
   "outputs": [],
   "source": [
    "def view_patients():\n",
    "    patient = pd.read_sql(\"Select * from Patients\",engine, index_col=[\"patient_id\"]) \n",
    "    return(patient)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 339,
   "id": "2db8a6fa-6dd2-4b12-a357-8b6c0768ece3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>patient_name</th>\n",
       "      <th>age</th>\n",
       "      <th>gender</th>\n",
       "      <th>address</th>\n",
       "      <th>contact_number</th>\n",
       "      <th>medical_history</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>patient_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Ramesh Iyer 2</td>\n",
       "      <td>52</td>\n",
       "      <td>Male</td>\n",
       "      <td>Jaipur</td>\n",
       "      <td>9899653422</td>\n",
       "      <td>None</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Deepika Reddy 3</td>\n",
       "      <td>82</td>\n",
       "      <td>Female</td>\n",
       "      <td>Hyderabad</td>\n",
       "      <td>9307924191</td>\n",
       "      <td>Asthma</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Priya Kapoor 4</td>\n",
       "      <td>77</td>\n",
       "      <td>Male</td>\n",
       "      <td>Chennai</td>\n",
       "      <td>9748276329</td>\n",
       "      <td>Corona</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Rahul Sharma 5</td>\n",
       "      <td>37</td>\n",
       "      <td>Male</td>\n",
       "      <td>Jaipur</td>\n",
       "      <td>9240114653</td>\n",
       "      <td>Asthma</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Pooja Thakur 6</td>\n",
       "      <td>77</td>\n",
       "      <td>Female</td>\n",
       "      <td>Pune</td>\n",
       "      <td>9148271369</td>\n",
       "      <td>Heart Disease</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>501</th>\n",
       "      <td>Roxx</td>\n",
       "      <td>28</td>\n",
       "      <td>Male</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>9375672652</td>\n",
       "      <td>Anxiety disorder</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>503</th>\n",
       "      <td>Roxxx</td>\n",
       "      <td>28</td>\n",
       "      <td>Male</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>9373472652</td>\n",
       "      <td>Anxiety disorder</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>505</th>\n",
       "      <td>Jazz</td>\n",
       "      <td>33</td>\n",
       "      <td>Male</td>\n",
       "      <td>Mumbai</td>\n",
       "      <td>9373472432</td>\n",
       "      <td>Night Blindness</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>506</th>\n",
       "      <td>Naina Singh</td>\n",
       "      <td>34</td>\n",
       "      <td>Female</td>\n",
       "      <td>Varansi</td>\n",
       "      <td>9876543765</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>507</th>\n",
       "      <td>Shaniel Reddy</td>\n",
       "      <td>43</td>\n",
       "      <td>Female</td>\n",
       "      <td>Possession</td>\n",
       "      <td>8798654634</td>\n",
       "      <td>Abnormal</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>504 rows × 6 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               patient_name  age  gender     address contact_number  \\\n",
       "patient_id                                                            \n",
       "2             Ramesh Iyer 2   52    Male      Jaipur     9899653422   \n",
       "3           Deepika Reddy 3   82  Female   Hyderabad     9307924191   \n",
       "4            Priya Kapoor 4   77    Male     Chennai     9748276329   \n",
       "5            Rahul Sharma 5   37    Male      Jaipur     9240114653   \n",
       "6            Pooja Thakur 6   77  Female        Pune     9148271369   \n",
       "...                     ...  ...     ...         ...            ...   \n",
       "501                    Roxx   28    Male      Mumbai     9375672652   \n",
       "503                   Roxxx   28    Male      Mumbai     9373472652   \n",
       "505                    Jazz   33    Male      Mumbai     9373472432   \n",
       "506             Naina Singh   34  Female     Varansi     9876543765   \n",
       "507           Shaniel Reddy   43  Female  Possession     8798654634   \n",
       "\n",
       "             medical_history  \n",
       "patient_id                    \n",
       "2                       None  \n",
       "3                     Asthma  \n",
       "4                     Corona  \n",
       "5                     Asthma  \n",
       "6              Heart Disease  \n",
       "...                      ...  \n",
       "501         Anxiety disorder  \n",
       "503         Anxiety disorder  \n",
       "505          Night Blindness  \n",
       "506                   Normal  \n",
       "507                 Abnormal  \n",
       "\n",
       "[504 rows x 6 columns]"
      ]
     },
     "execution_count": 339,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "view_patients()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "80025f18-e162-46c4-926c-4189a1296e8e",
   "metadata": {},
   "source": [
    "### Adding New patients :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 241,
   "id": "136caebe-6dd8-4b66-8f3d-77f9438fd5c0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_patient():\n",
    "    patient_name = input(\"Enter Patient Name: \")\n",
    "    age = input(\"Enter Age: \")\n",
    "    gender = input(\"Enter Gender (M/F): \")\n",
    "    contact_number = input(\"Enter Contact Number: \")\n",
    "    medical_history = input(\"Enter Medical_history: \")\n",
    "    address = input(\"Enter Address: \")\n",
    "    \n",
    "    query = \"INSERT INTO patients (patient_name, age, gender, address,\tcontact_number,\tmedical_history) VALUES (%s, %s, %s, %s, %s, %s)\"\n",
    "\n",
    "    values = (patient_name, age, gender, address, contact_number, medical_history)\n",
    "    cursor.execute(query, values)\n",
    "    conn.commit()\n",
    "    print(\"Patient added successfully!\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4e6c883f-68a9-4aa3-88c0-8b00864e0bb7",
   "metadata": {},
   "source": [
    "### Updating Medical_History :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 349,
   "id": "e6439138-0fa6-4d68-ba6f-896e1452078c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_patient():\n",
    "    patient_id = input(\"Enter Patient_id :\")\n",
    "    medical_history = input(\"Enter Disease :\")\n",
    "    query = \"UPDATE patients SET medical_history = %s WHERE patient_id = %s\"\n",
    "    values = (medical_history, patient_id)\n",
    "    cursor.execute(query, values)\n",
    "    conn.commit()\n",
    "    print(f\"Patient ID {patient_id} updated successfully!\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 351,
   "id": "8fedb44e-2e27-465b-bd2c-ed3f2b490941",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Patient_id : 34\n",
      "Enter Disease : corona\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Patient ID 34 updated successfully!\n"
     ]
    }
   ],
   "source": [
    "update_patient()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "acf7d07b-865a-4d22-9a75-e3deca5c8af4",
   "metadata": {},
   "source": [
    "### Deleting Patient Details :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 363,
   "id": "66af0167-a8bf-41c8-9da8-3f209ff8bb8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def delete_patient():\n",
    "    patient_id = input(\"Enter Patient_id No -\")\n",
    "    query = \"DELETE FROM patients WHERE patient_id = %s\"\n",
    "    values = (patient_id,)\n",
    "    cursor.execute(query, values)\n",
    "    conn.commit()\n",
    "    print(f\"Patient ID {patient_id} deleted successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 367,
   "id": "8e8d3886-415b-4e78-81cd-d0523c732d54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter Patient_id No - 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Patient ID 1 deleted successfully!\n"
     ]
    }
   ],
   "source": [
    "delete_patient()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b64a2637-797e-40a7-abfc-d47016eab9de",
   "metadata": {},
   "source": [
    "### Function to manage patients :\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 306,
   "id": "15583db7-af5b-4e45-ba40-1c51186479ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def manage_patients():\n",
    "    print(\"\\n--- Patient Management ---\")\n",
    "    print(\"1. Add Patient\")\n",
    "    print(\"2. View Patients\")\n",
    "    print(\"3. Update Patient\")\n",
    "    print(\"4. Delete Patient\")\n",
    "    choice = input(\"Enter your choice: \")\n",
    "    \n",
    "    if choice == \"1\":\n",
    "        add_patient()\n",
    "    elif choice == \"2\":\n",
    "        return(view_patients())\n",
    "    elif choice == \"3\":\n",
    "        update_patient()\n",
    "    elif choice == \"4\":\n",
    "        delete_patient()\n",
    "    else:\n",
    "        print(\"Invalid choice! Returning to main menu.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 415,
   "id": "92ffd346-ac39-48bc-9dcf-7da850e5d59d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Patient Management ---\n",
      "1. Add Patient\n",
      "2. View Patients\n",
      "3. Update Patient\n",
      "4. Delete Patient\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n",
      "Enter Patient_id No - 1\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Patient ID 1 deleted successfully!\n"
     ]
    }
   ],
   "source": [
    "manage_patients()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e13e8215-e933-476b-a25b-df9209cd38b0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a356f3de-08b7-4eb9-872f-ce20374537e8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "0bfab951-18fb-4b69-b330-88d1e1ee1e7f",
   "metadata": {},
   "source": [
    "## Retrieving Doctors Table :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 441,
   "id": "740eeda4-520a-4e3b-9440-05927a7aca5c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def view_doctor():\n",
    "    doctor_df = pd.read_sql(\"Select * from Doctors\",engine,index_col=[\"Dr_id\"])\n",
    "    return(doctor_df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 445,
   "id": "64f1260d-e196-4962-90cf-1ce954ac261a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Dr_name</th>\n",
       "      <th>specialization</th>\n",
       "      <th>contact_number</th>\n",
       "      <th>availability</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Dr_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Dr. Sameer Khan 1</td>\n",
       "      <td>Neurologist</td>\n",
       "      <td>9106026779</td>\n",
       "      <td>10 AM - 6 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Dr. Kunal Sharma 2</td>\n",
       "      <td>General Physician</td>\n",
       "      <td>9191537940</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Dr. Rohan Malhotra 3</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9298201934</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Dr. Sameer Khan 4</td>\n",
       "      <td>Cardiologist</td>\n",
       "      <td>9598207477</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Dr. Vikram Sinha 5</td>\n",
       "      <td>Psychiatrist</td>\n",
       "      <td>9344413285</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Dr. Meena Reddy 6</td>\n",
       "      <td>Neurologist</td>\n",
       "      <td>9486598954</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>Dr. Sameer Khan 7</td>\n",
       "      <td>Oncologist</td>\n",
       "      <td>9643258922</td>\n",
       "      <td>11 AM - 7 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>Dr. Rohan Malhotra 8</td>\n",
       "      <td>Cardiologist</td>\n",
       "      <td>9464786603</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>Dr. Meena Reddy 9</td>\n",
       "      <td>General Physician</td>\n",
       "      <td>9146103537</td>\n",
       "      <td>10 AM - 6 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>Dr. Rohan Malhotra 10</td>\n",
       "      <td>Ophthalmologist</td>\n",
       "      <td>9092012662</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>Dr. Rohan Malhotra 11</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9973327572</td>\n",
       "      <td>10 AM - 6 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>Dr. Sameer Khan 12</td>\n",
       "      <td>Orthopedic</td>\n",
       "      <td>9475564519</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>Dr. Aditi Joshi 13</td>\n",
       "      <td>Dermatologist</td>\n",
       "      <td>9186335216</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>Dr. Anjali Mehta 14</td>\n",
       "      <td>Pediatrician</td>\n",
       "      <td>9011280556</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>Dr. Meena Reddy 15</td>\n",
       "      <td>Psychiatrist</td>\n",
       "      <td>9814381699</td>\n",
       "      <td>10 AM - 6 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>Dr. Sunita Das 16</td>\n",
       "      <td>Dermatologist</td>\n",
       "      <td>9654318829</td>\n",
       "      <td>11 AM - 7 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>Dr. Pooja Desai 17</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9784774237</td>\n",
       "      <td>10 AM - 6 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>Dr. Sameer Khan 18</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9569084015</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>Dr. Rajiv Nair 19</td>\n",
       "      <td>Oncologist</td>\n",
       "      <td>9097018615</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>Dr. Meena Reddy 20</td>\n",
       "      <td>Orthopedic</td>\n",
       "      <td>9674839642</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>Dr. Sameer Khan 21</td>\n",
       "      <td>Psychiatrist</td>\n",
       "      <td>9987688900</td>\n",
       "      <td>11 AM - 7 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>Dr. Pooja Desai 22</td>\n",
       "      <td>Pediatrician</td>\n",
       "      <td>9317413374</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>Dr. Pooja Desai 23</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9488821681</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>Dr. Pooja Desai 24</td>\n",
       "      <td>Ophthalmologist</td>\n",
       "      <td>9676689434</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>Dr. Kunal Sharma 25</td>\n",
       "      <td>Oncologist</td>\n",
       "      <td>9406341625</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>Dr. Aditi Joshi 26</td>\n",
       "      <td>Neurologist</td>\n",
       "      <td>9565316755</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>Dr. Vikram Sinha 27</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9149739034</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>Dr. Rohan Malhotra 28</td>\n",
       "      <td>Psychiatrist</td>\n",
       "      <td>9238801627</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>Dr. Meena Reddy 29</td>\n",
       "      <td>General Physician</td>\n",
       "      <td>9842873456</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>Dr. Sunita Das 30</td>\n",
       "      <td>Oncologist</td>\n",
       "      <td>9548531318</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>Dr. Rohan Malhotra 31</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9846374721</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>Dr. Kunal Sharma 32</td>\n",
       "      <td>Dermatologist</td>\n",
       "      <td>9479042282</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>Dr. Aditi Joshi 33</td>\n",
       "      <td>Neurologist</td>\n",
       "      <td>9571857051</td>\n",
       "      <td>10 AM - 6 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>Dr. Aditi Joshi 34</td>\n",
       "      <td>Cardiologist</td>\n",
       "      <td>9046368797</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>Dr. Rajiv Nair 35</td>\n",
       "      <td>Neurologist</td>\n",
       "      <td>9452203650</td>\n",
       "      <td>11 AM - 7 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>Dr. Aditi Joshi 36</td>\n",
       "      <td>Psychiatrist</td>\n",
       "      <td>9817498123</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>Dr. Sunita Das 37</td>\n",
       "      <td>Dermatologist</td>\n",
       "      <td>9047269378</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>Dr. Meena Reddy 38</td>\n",
       "      <td>Oncologist</td>\n",
       "      <td>9380865715</td>\n",
       "      <td>10 AM - 6 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>Dr. Vikram Sinha 39</td>\n",
       "      <td>Pediatrician</td>\n",
       "      <td>9759239751</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>Dr. Kunal Sharma 40</td>\n",
       "      <td>Ophthalmologist</td>\n",
       "      <td>9135590200</td>\n",
       "      <td>11 AM - 7 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>Dr. Pooja Desai 41</td>\n",
       "      <td>General Physician</td>\n",
       "      <td>9372180080</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>Dr. Rajiv Nair 42</td>\n",
       "      <td>Psychiatrist</td>\n",
       "      <td>9304688245</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>Dr. Anjali Mehta 43</td>\n",
       "      <td>Dermatologist</td>\n",
       "      <td>9153194207</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>Dr. Kunal Sharma 44</td>\n",
       "      <td>Pediatrician</td>\n",
       "      <td>9573026415</td>\n",
       "      <td>9 AM - 3 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>Dr. Kunal Sharma 45</td>\n",
       "      <td>General Physician</td>\n",
       "      <td>9735678503</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>Dr. Sameer Khan 46</td>\n",
       "      <td>Orthopedic</td>\n",
       "      <td>9238863147</td>\n",
       "      <td>11 AM - 7 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>Dr. Anjali Mehta 47</td>\n",
       "      <td>Psychiatrist</td>\n",
       "      <td>9151874426</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>Dr. Meena Reddy 48</td>\n",
       "      <td>General Physician</td>\n",
       "      <td>9905558113</td>\n",
       "      <td>9 AM - 5 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>Dr. Vikram Sinha 49</td>\n",
       "      <td>Pediatrician</td>\n",
       "      <td>9339940241</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50</th>\n",
       "      <td>Dr. Kunal Sharma 50</td>\n",
       "      <td>ENT Specialist</td>\n",
       "      <td>9431514111</td>\n",
       "      <td>8 AM - 4 PM</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>51</th>\n",
       "      <td>Sajid kamath</td>\n",
       "      <td>Counselling</td>\n",
       "      <td>9387678947</td>\n",
       "      <td>7pm - 11pm</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                     Dr_name     specialization contact_number  availability\n",
       "Dr_id                                                                       \n",
       "1          Dr. Sameer Khan 1        Neurologist     9106026779  10 AM - 6 PM\n",
       "2         Dr. Kunal Sharma 2  General Physician     9191537940   9 AM - 5 PM\n",
       "3       Dr. Rohan Malhotra 3     ENT Specialist     9298201934   9 AM - 3 PM\n",
       "4          Dr. Sameer Khan 4       Cardiologist     9598207477   9 AM - 5 PM\n",
       "5         Dr. Vikram Sinha 5       Psychiatrist     9344413285   9 AM - 3 PM\n",
       "6          Dr. Meena Reddy 6        Neurologist     9486598954   9 AM - 3 PM\n",
       "7          Dr. Sameer Khan 7         Oncologist     9643258922  11 AM - 7 PM\n",
       "8       Dr. Rohan Malhotra 8       Cardiologist     9464786603   9 AM - 3 PM\n",
       "9          Dr. Meena Reddy 9  General Physician     9146103537  10 AM - 6 PM\n",
       "10     Dr. Rohan Malhotra 10    Ophthalmologist     9092012662   8 AM - 4 PM\n",
       "11     Dr. Rohan Malhotra 11     ENT Specialist     9973327572  10 AM - 6 PM\n",
       "12        Dr. Sameer Khan 12         Orthopedic     9475564519   9 AM - 3 PM\n",
       "13        Dr. Aditi Joshi 13      Dermatologist     9186335216   9 AM - 3 PM\n",
       "14       Dr. Anjali Mehta 14       Pediatrician     9011280556   9 AM - 3 PM\n",
       "15        Dr. Meena Reddy 15       Psychiatrist     9814381699  10 AM - 6 PM\n",
       "16         Dr. Sunita Das 16      Dermatologist     9654318829  11 AM - 7 PM\n",
       "17        Dr. Pooja Desai 17     ENT Specialist     9784774237  10 AM - 6 PM\n",
       "18        Dr. Sameer Khan 18     ENT Specialist     9569084015   8 AM - 4 PM\n",
       "19         Dr. Rajiv Nair 19         Oncologist     9097018615   9 AM - 3 PM\n",
       "20        Dr. Meena Reddy 20         Orthopedic     9674839642   8 AM - 4 PM\n",
       "21        Dr. Sameer Khan 21       Psychiatrist     9987688900  11 AM - 7 PM\n",
       "22        Dr. Pooja Desai 22       Pediatrician     9317413374   8 AM - 4 PM\n",
       "23        Dr. Pooja Desai 23     ENT Specialist     9488821681   9 AM - 3 PM\n",
       "24        Dr. Pooja Desai 24    Ophthalmologist     9676689434   9 AM - 3 PM\n",
       "25       Dr. Kunal Sharma 25         Oncologist     9406341625   9 AM - 5 PM\n",
       "26        Dr. Aditi Joshi 26        Neurologist     9565316755   9 AM - 3 PM\n",
       "27       Dr. Vikram Sinha 27     ENT Specialist     9149739034   9 AM - 3 PM\n",
       "28     Dr. Rohan Malhotra 28       Psychiatrist     9238801627   9 AM - 5 PM\n",
       "29        Dr. Meena Reddy 29  General Physician     9842873456   8 AM - 4 PM\n",
       "30         Dr. Sunita Das 30         Oncologist     9548531318   9 AM - 5 PM\n",
       "31     Dr. Rohan Malhotra 31     ENT Specialist     9846374721   9 AM - 5 PM\n",
       "32       Dr. Kunal Sharma 32      Dermatologist     9479042282   9 AM - 3 PM\n",
       "33        Dr. Aditi Joshi 33        Neurologist     9571857051  10 AM - 6 PM\n",
       "34        Dr. Aditi Joshi 34       Cardiologist     9046368797   8 AM - 4 PM\n",
       "35         Dr. Rajiv Nair 35        Neurologist     9452203650  11 AM - 7 PM\n",
       "36        Dr. Aditi Joshi 36       Psychiatrist     9817498123   9 AM - 3 PM\n",
       "37         Dr. Sunita Das 37      Dermatologist     9047269378   9 AM - 3 PM\n",
       "38        Dr. Meena Reddy 38         Oncologist     9380865715  10 AM - 6 PM\n",
       "39       Dr. Vikram Sinha 39       Pediatrician     9759239751   8 AM - 4 PM\n",
       "40       Dr. Kunal Sharma 40    Ophthalmologist     9135590200  11 AM - 7 PM\n",
       "41        Dr. Pooja Desai 41  General Physician     9372180080   9 AM - 3 PM\n",
       "42         Dr. Rajiv Nair 42       Psychiatrist     9304688245   9 AM - 3 PM\n",
       "43       Dr. Anjali Mehta 43      Dermatologist     9153194207   9 AM - 5 PM\n",
       "44       Dr. Kunal Sharma 44       Pediatrician     9573026415   9 AM - 3 PM\n",
       "45       Dr. Kunal Sharma 45  General Physician     9735678503   8 AM - 4 PM\n",
       "46        Dr. Sameer Khan 46         Orthopedic     9238863147  11 AM - 7 PM\n",
       "47       Dr. Anjali Mehta 47       Psychiatrist     9151874426   9 AM - 5 PM\n",
       "48        Dr. Meena Reddy 48  General Physician     9905558113   9 AM - 5 PM\n",
       "49       Dr. Vikram Sinha 49       Pediatrician     9339940241   8 AM - 4 PM\n",
       "50       Dr. Kunal Sharma 50     ENT Specialist     9431514111   8 AM - 4 PM\n",
       "51              Sajid kamath        Counselling     9387678947    7pm - 11pm"
      ]
     },
     "execution_count": 445,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "view_doctor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 431,
   "id": "1553e2bd-0f0f-4825-af23-817b01c3dfd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "def add_doctor():\n",
    "    Dr_name = input(\" Dr. Name :\")\n",
    "    specialization = input(\"specialization :\")\n",
    "    contact_number = input(\"Contact number :\")\n",
    "    availability = input(\"Availability :\")\n",
    "    query = \"Insert into doctors(Dr_name, specialization, contact_number, availability) values(%s,%s,%s,%s)\"\n",
    "    values = (Dr_name, specialization, contact_number, availability)\n",
    "    cursor.execute(query, values)\n",
    "    conn.commit()\n",
    "    print(\"Added Successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 429,
   "id": "24b08127-b99a-46da-8473-97b0cff02204",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " Dr. Name : Sajid kamath\n",
      " specialization : Counselling\n",
      "Contact number : 9387678947\n",
      "Availability : 7pm - 11pm\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Added Successfully\n"
     ]
    }
   ],
   "source": [
    "add_doctor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 467,
   "id": "c5499bc1-3e04-49af-832d-5f25add82d02",
   "metadata": {},
   "outputs": [],
   "source": [
    "def delete_doctor():\n",
    "    Dr_id = input(\"Dr.id -\")\n",
    "    query = \"delete from Doctors where Dr_id = %s\"\n",
    "    values = (Dr_id,)\n",
    "    cursor.execute(query,values)\n",
    "    conn.commit()\n",
    "    print(\"Doctor details deleted successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 469,
   "id": "b57276cd-836e-4542-8f1b-b2c9411e07be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Dr.id - 51\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Doctor details deleted successfully\n"
     ]
    }
   ],
   "source": [
    "delete_doctor()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "326ec237-0edd-49c9-972c-5c53ee61390b",
   "metadata": {},
   "source": [
    "### Function to Manage Doctors :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 453,
   "id": "afbc6f33-a7e4-43bc-9e48-d18b5d5397fc",
   "metadata": {},
   "outputs": [],
   "source": [
    "def manage_doctors():\n",
    "    print(\"\\n--- Doctors Management ---\")\n",
    "    print(\"1.View Doctors\")\n",
    "    print(\"2.Add Doctor\")\n",
    "    print(\"3.Delete Doctor\")\n",
    "    choice = input(\"Choose Option\")\n",
    "    \n",
    "    if choice == \"1\":\n",
    "        return(view_doctor())\n",
    "    elif choice == \"2\":\n",
    "        add_doctor()\n",
    "    elif choice == \"3\":\n",
    "        delete_doctor()\n",
    "    else:\n",
    "        print(\"Invalid choice! Returning to main menu.\")\n",
    "\n",
    "    \n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1ae9c86-4084-4690-bcbe-00e9d58236a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "manage_doctors()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "45a35e5b-30c6-4479-a728-6875962e3dc3",
   "metadata": {},
   "source": [
    "## Retrieving Appointments Table :\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "7c5802e7-fea5-4347-acef-d7e11ab722ed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>patient_id</th>\n",
       "      <th>doctor_id</th>\n",
       "      <th>appointment_date</th>\n",
       "      <th>status</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>appointment_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>444</td>\n",
       "      <td>12</td>\n",
       "      <td>2025-03-15</td>\n",
       "      <td>Cancelled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>232</td>\n",
       "      <td>8</td>\n",
       "      <td>2025-10-05</td>\n",
       "      <td>Cancelled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>353</td>\n",
       "      <td>38</td>\n",
       "      <td>2025-12-22</td>\n",
       "      <td>Completed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>122</td>\n",
       "      <td>48</td>\n",
       "      <td>2025-08-10</td>\n",
       "      <td>Completed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>439</td>\n",
       "      <td>7</td>\n",
       "      <td>2025-04-04</td>\n",
       "      <td>Completed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>996</th>\n",
       "      <td>69</td>\n",
       "      <td>48</td>\n",
       "      <td>2025-01-01</td>\n",
       "      <td>Completed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>997</th>\n",
       "      <td>62</td>\n",
       "      <td>47</td>\n",
       "      <td>2025-11-07</td>\n",
       "      <td>Cancelled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>998</th>\n",
       "      <td>404</td>\n",
       "      <td>50</td>\n",
       "      <td>2025-01-25</td>\n",
       "      <td>Cancelled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>999</th>\n",
       "      <td>171</td>\n",
       "      <td>18</td>\n",
       "      <td>2025-01-13</td>\n",
       "      <td>Scheduled</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1000</th>\n",
       "      <td>408</td>\n",
       "      <td>49</td>\n",
       "      <td>2025-08-09</td>\n",
       "      <td>Cancelled</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1000 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                patient_id  doctor_id appointment_date     status\n",
       "appointment_id                                                   \n",
       "1                      444         12       2025-03-15  Cancelled\n",
       "2                      232          8       2025-10-05  Cancelled\n",
       "3                      353         38       2025-12-22  Completed\n",
       "4                      122         48       2025-08-10  Completed\n",
       "5                      439          7       2025-04-04  Completed\n",
       "...                    ...        ...              ...        ...\n",
       "996                     69         48       2025-01-01  Completed\n",
       "997                     62         47       2025-11-07  Cancelled\n",
       "998                    404         50       2025-01-25  Cancelled\n",
       "999                    171         18       2025-01-13  Scheduled\n",
       "1000                   408         49       2025-08-09  Cancelled\n",
       "\n",
       "[1000 rows x 4 columns]"
      ]
     },
     "execution_count": 71,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Appointment_df = pd.read_sql(\"Select * from appointments\", engine,index_col = [\"appointment_id\"])\n",
    "Appointment_df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9e39b37c-2bbc-401c-ace5-d02ed14eaca8",
   "metadata": {},
   "source": [
    "### Inserting New Appointments :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "4acb5f23-e669-4e65-bdd1-ba7cdc6960b0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def insert_appointments(patient_id, doctor_id, appointment_date, status):\n",
    "    query = \"Insert into Appointments(patient_id, doctor_id, appointment_date, status) values(%s,%s,%s,%s)\"\n",
    "    values = (patient_id, doctor_id, appointment_date, status)\n",
    "    cursor.execute(query,values)\n",
    "    conn.commit()\n",
    "    print(f\"Appointment Registered Successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "857b143e-f80f-4ec4-8f6d-7aa7f3565473",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Appointment Registered Successfully\n"
     ]
    }
   ],
   "source": [
    "insert_appointments(501,23, \"2025-2-28\", \"Scheduled\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2791663b-b228-4a7b-b575-8884ce135c53",
   "metadata": {},
   "source": [
    "### Updating Appointments"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "id": "cf686ffe-68f6-4c2f-988a-fcfe42defe3a",
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_appointment(patient_id, status):\n",
    "    query = \"update appointments SET status = %s where patient_id = %s\"\n",
    "    values= (status, patient_id)\n",
    "    cursor.execute(query, values)\n",
    "    conn.commit()\n",
    "    print(\"Appointment Status Updated\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 93,
   "id": "f075efef-4695-429e-96dd-faae659f9732",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Appointment Status Updated\n"
     ]
    }
   ],
   "source": [
    "update_appointment(501,\"Scheduled\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6095bfc-b7e6-4a3b-8bca-8828b8a309e7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40f0ab4f-ea55-420a-9327-5b00e960e501",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "09321872-71ff-4cce-ad2a-34b6ce27def3",
   "metadata": {},
   "source": [
    "## Retrieving Billing Table :\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "id": "576ce6b3-a3e3-4f0c-8c24-1349c303fccf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>patient_id</th>\n",
       "      <th>appointment_id</th>\n",
       "      <th>total_amount</th>\n",
       "      <th>payment_status</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Bill_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>175</td>\n",
       "      <td>745</td>\n",
       "      <td>719.0</td>\n",
       "      <td>Pending</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>198</td>\n",
       "      <td>177</td>\n",
       "      <td>4458.0</td>\n",
       "      <td>Pending</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>144</td>\n",
       "      <td>72</td>\n",
       "      <td>3026.0</td>\n",
       "      <td>Failed</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>304</td>\n",
       "      <td>505</td>\n",
       "      <td>1684.0</td>\n",
       "      <td>Pending</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>194</td>\n",
       "      <td>32</td>\n",
       "      <td>3241.0</td>\n",
       "      <td>Paid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>696</th>\n",
       "      <td>348</td>\n",
       "      <td>879</td>\n",
       "      <td>4948.0</td>\n",
       "      <td>Pending</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>697</th>\n",
       "      <td>413</td>\n",
       "      <td>590</td>\n",
       "      <td>3908.0</td>\n",
       "      <td>Pending</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>698</th>\n",
       "      <td>87</td>\n",
       "      <td>298</td>\n",
       "      <td>2540.0</td>\n",
       "      <td>Paid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>699</th>\n",
       "      <td>445</td>\n",
       "      <td>896</td>\n",
       "      <td>4329.0</td>\n",
       "      <td>Paid</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>700</th>\n",
       "      <td>162</td>\n",
       "      <td>934</td>\n",
       "      <td>4610.0</td>\n",
       "      <td>Paid</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>699 rows × 4 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "         patient_id  appointment_id  total_amount payment_status\n",
       "Bill_id                                                         \n",
       "1               175             745         719.0        Pending\n",
       "2               198             177        4458.0        Pending\n",
       "3               144              72        3026.0         Failed\n",
       "4               304             505        1684.0        Pending\n",
       "5               194              32        3241.0           Paid\n",
       "...             ...             ...           ...            ...\n",
       "696             348             879        4948.0        Pending\n",
       "697             413             590        3908.0        Pending\n",
       "698              87             298        2540.0           Paid\n",
       "699             445             896        4329.0           Paid\n",
       "700             162             934        4610.0           Paid\n",
       "\n",
       "[699 rows x 4 columns]"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Billing_df = pd.read_sql(\"Select * from billing\",engine,index_col=[\"Bill_id\"])\n",
    "Billing_df\n",
    "                        \n",
    "                        "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e052f30c-6857-44c3-baea-cec62d42cdb1",
   "metadata": {},
   "source": [
    "### Inserting New Bills :\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 103,
   "id": "dc332667-8a90-43df-a981-8975c5838527",
   "metadata": {},
   "outputs": [],
   "source": [
    "def insert_new_bill(patient_id,\tappointment_id,\ttotal_amount, payment_status):\n",
    "    query = \"Insert into Billing(patient_id, appointment_id, total_amount, payment_status) Values(%s,%s,%s,%s)\"\n",
    "    values = (patient_id,\tappointment_id,\ttotal_amount, payment_status)\n",
    "    cursor.execute(query, values)\n",
    "    conn.commit()\n",
    "    print(\"New Bill Inserted\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 107,
   "id": "bb497605-509e-427a-a631-670d000f8c74",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "New Bill Inserted\n"
     ]
    }
   ],
   "source": [
    "insert_new_bill(501,32,3000,\"Paid\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "412905e8-bedc-47f6-a97a-56131520b2f8",
   "metadata": {},
   "source": [
    "#### Groupby Function on Billing :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 127,
   "id": "baf05e24-8dc4-4d9a-8184-4b7cc03491c6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th>total_amount</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>patient_id</th>\n",
       "      <th>payment_status</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <th>Pending</th>\n",
       "      <td>531.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <th>Paid</th>\n",
       "      <td>1962.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <th>Pending</th>\n",
       "      <td>3689.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <th>Paid</th>\n",
       "      <td>1635.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <th>Failed</th>\n",
       "      <td>2613.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">494</th>\n",
       "      <th>Failed</th>\n",
       "      <td>719.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Pending</th>\n",
       "      <td>4168.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th rowspan=\"2\" valign=\"top\">495</th>\n",
       "      <th>Failed</th>\n",
       "      <td>1553.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Paid</th>\n",
       "      <td>4416.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>498</th>\n",
       "      <th>Paid</th>\n",
       "      <td>4268.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>555 rows × 1 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "                           total_amount\n",
       "patient_id payment_status              \n",
       "5          Pending                531.0\n",
       "6          Paid                  1962.0\n",
       "7          Pending               3689.0\n",
       "8          Paid                  1635.0\n",
       "9          Failed                2613.0\n",
       "...                                 ...\n",
       "494        Failed                 719.0\n",
       "           Pending               4168.0\n",
       "495        Failed                1553.0\n",
       "           Paid                  4416.0\n",
       "498        Paid                  4268.0\n",
       "\n",
       "[555 rows x 1 columns]"
      ]
     },
     "execution_count": 127,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Billing_df.groupby(by=[\"patient_id\",\"payment_status\"])[[\"total_amount\"]].sum()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2de0593d-f2f4-4e12-96b6-e507e6a44b78",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad24bfae-32c6-4612-bc87-8a412c04339d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "c0be5097-7795-4006-b4ab-1b0c31723faa",
   "metadata": {},
   "source": [
    "## Retrieving Medicalrecords Table :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 154,
   "id": "7251023b-dbf5-4a0c-9a72-140d202cdfd4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>patient_id</th>\n",
       "      <th>doctor_id</th>\n",
       "      <th>diagnosis</th>\n",
       "      <th>prescription</th>\n",
       "      <th>test_results</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>record_id</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>233</td>\n",
       "      <td>34</td>\n",
       "      <td>None</td>\n",
       "      <td>Vitamin Supplements</td>\n",
       "      <td>X-ray positive</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>142</td>\n",
       "      <td>10</td>\n",
       "      <td>Diabetes</td>\n",
       "      <td>Vitamin Supplements</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>114</td>\n",
       "      <td>44</td>\n",
       "      <td>Diabetes</td>\n",
       "      <td>Medicine A, Medicine B</td>\n",
       "      <td>Blood test abnormal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>199</td>\n",
       "      <td>27</td>\n",
       "      <td>None</td>\n",
       "      <td>Medicine A, Medicine B</td>\n",
       "      <td>Abnormal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>106</td>\n",
       "      <td>40</td>\n",
       "      <td>Migraine</td>\n",
       "      <td>Painkillers, Rest</td>\n",
       "      <td>Blood test abnormal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>796</th>\n",
       "      <td>192</td>\n",
       "      <td>46</td>\n",
       "      <td>Diabetes</td>\n",
       "      <td>Antibiotics, Rest</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>797</th>\n",
       "      <td>500</td>\n",
       "      <td>50</td>\n",
       "      <td>Fracture</td>\n",
       "      <td>Painkillers, Rest</td>\n",
       "      <td>Blood test abnormal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>798</th>\n",
       "      <td>333</td>\n",
       "      <td>25</td>\n",
       "      <td>Diabetes</td>\n",
       "      <td>Vitamin Supplements</td>\n",
       "      <td>Normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>799</th>\n",
       "      <td>74</td>\n",
       "      <td>45</td>\n",
       "      <td>Skin Allergy</td>\n",
       "      <td>Vitamin Supplements</td>\n",
       "      <td>MRI normal</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>800</th>\n",
       "      <td>390</td>\n",
       "      <td>43</td>\n",
       "      <td>Hypertension</td>\n",
       "      <td>Vitamin Supplements</td>\n",
       "      <td>X-ray positive</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>796 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           patient_id  doctor_id     diagnosis            prescription  \\\n",
       "record_id                                                                \n",
       "1                 233         34          None     Vitamin Supplements   \n",
       "2                 142         10      Diabetes     Vitamin Supplements   \n",
       "3                 114         44      Diabetes  Medicine A, Medicine B   \n",
       "4                 199         27          None  Medicine A, Medicine B   \n",
       "5                 106         40      Migraine       Painkillers, Rest   \n",
       "...               ...        ...           ...                     ...   \n",
       "796               192         46      Diabetes       Antibiotics, Rest   \n",
       "797               500         50      Fracture       Painkillers, Rest   \n",
       "798               333         25      Diabetes     Vitamin Supplements   \n",
       "799                74         45  Skin Allergy     Vitamin Supplements   \n",
       "800               390         43  Hypertension     Vitamin Supplements   \n",
       "\n",
       "                  test_results  \n",
       "record_id                       \n",
       "1               X-ray positive  \n",
       "2                       Normal  \n",
       "3          Blood test abnormal  \n",
       "4                     Abnormal  \n",
       "5          Blood test abnormal  \n",
       "...                        ...  \n",
       "796                     Normal  \n",
       "797        Blood test abnormal  \n",
       "798                     Normal  \n",
       "799                 MRI normal  \n",
       "800             X-ray positive  \n",
       "\n",
       "[796 rows x 5 columns]"
      ]
     },
     "execution_count": 154,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Medicalrecords_df = pd.read_sql(\"Select * from medicalrecords\",engine, index_col=[\"record_id\"])\n",
    "Medicalrecords_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 176,
   "id": "30f23d1e-f87f-4585-9762-0d95bb46bbe0",
   "metadata": {},
   "outputs": [],
   "source": [
    "def insert_medrecords( patient_id, doctor_id, diagnosis, prescription,\ttest_results):\n",
    "    query = \"Insert into medicalrecords(patient_id, doctor_id, diagnosis, prescription,\ttest_results) Values(%s,%s,%s,%s,%s)\"\n",
    "    Values = (patient_id, doctor_id, diagnosis, prescription,\ttest_results)\n",
    "    cursor.execute(query, Values)\n",
    "    conn.commit()\n",
    "    print(\"Medrecords Added Successfully\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 197,
   "id": "aea5d71a-f04b-410c-b267-330f816e77da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Medrecords Added Successfully\n"
     ]
    }
   ],
   "source": [
    "insert_medrecords(10,34,\"Alziemer\", \"Take rest, fluoxenithine\", \"Abnormal\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 201,
   "id": "94dcd2bc-8f7b-4c0f-993e-0a5861bd4a2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def update_medrecords(diagnosis, prescription,record_id, patient_id):\n",
    "    query = \"UPDATE medicalrecords SET diagnosis = %s, prescription = %s WHERE record_id = %s AND patient_id = %s\"\n",
    "    values =  (diagnosis, prescription,record_id, patient_id)\n",
    "    cursor.execute(query, values)\n",
    "    conn.commit()\n",
    "    print(\"Updated Successfully\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 203,
   "id": "9870541e-d673-475a-92dd-c7b6d425cc3e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Updated Successfully\n"
     ]
    }
   ],
   "source": [
    "update_medrecords(\"Depression\", \"Counselling\",800 , 390)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a8f3f6b-7f94-4d30-9476-c8a6f4b09f7a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "ca5a455c-232e-4cdf-8271-f7478cf39341",
   "metadata": {},
   "source": [
    "# Setting up Menu Function :"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 213,
   "id": "a58c309e-17ec-49a3-bf9b-c2da4b94c715",
   "metadata": {},
   "outputs": [],
   "source": [
    "def display_menu():\n",
    "    print(\"\\n===== HOSPITAL MANAGEMENT SYSTEM =====\")\n",
    "    print(\"1. Manage Patients\")\n",
    "    print(\"2. Manage Doctors\")\n",
    "    print(\"3. Manage Appointments\")\n",
    "    print(\"4. Manage Billing\")\n",
    "    print(\"5. Manage MedicalRecords\")\n",
    "    print(\"6. Exit\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 215,
   "id": "34ad1f24-b75a-4b22-bbc1-4038dd83405e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== HOSPITAL MANAGEMENT SYSTEM =====\n",
      "1. Manage Patients\n",
      "2. Manage Doctors\n",
      "3. Manage Appointments\n",
      "4. Manage Billing\n",
      "5. Manage MedicalRecords\n",
      "6. Exit\n"
     ]
    }
   ],
   "source": [
    "display_menu()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96e73ca0-935c-4249-b67c-983474d8947b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "ce410845-9f88-41c3-beb6-9b982b64292a",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 373,
   "id": "6feb0d43-4017-4d4d-99b5-7c5b025dff4b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "--- Patient Management ---\n",
      "1. Add Patient\n",
      "2. View Patients\n",
      "3. Update Patient\n",
      "4. Delete Patient\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter your choice:  4\n",
      "Enter Patient_id No - 88\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Patient ID 88 deleted successfully!\n"
     ]
    }
   ],
   "source": [
    "manage_patients()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "319e7fa6-af8f-4c76-b13b-c1d3e6dfdcf9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a5c1701-fb00-4cbd-9d6e-efbddef9f9ed",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b67d5a32-c438-431f-83e9-8ee0cd82a589",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a24aeb39-5d24-4905-81e5-c7a3e143a3b9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "accf8da2-4bf4-4d3e-8799-6412a4e8d3f9",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e0c335e6-c93c-4add-aad6-231ce2b120d7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0eb36bff-a46b-434c-b993-250efef4a382",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "00bf217d-9de5-435d-a756-d5be4d8f4909",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2fc78c66-9262-4221-a015-59793831a0ef",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8934987-b36b-456f-b085-c7588cad1594",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "70caf686-fb35-44bf-9445-17b0562089ae",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e56e042-6159-4047-9952-533d972a6acd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27d3ec0f-4a3d-4937-83aa-08ae2f9bd49f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c7dd70a4-7002-4cb1-94c4-bed3d152812b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8ac50aa8-3fcf-493a-87c8-b64f03e99649",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2aed3f45-7b4d-4234-bfbb-94ca7f9ccf86",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ea49c022-7cfe-42a8-8e33-20c3f38d97ef",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf30d9d7-a8c7-4b6b-850f-1430f86576b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af55cc33-0cf8-40d9-b414-bd54ab17d8b8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8690cd4-5e59-4331-901e-996269c225cf",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3aa8283b-2fa7-4692-a180-24ae00c6ee59",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c4706b3-9f73-482b-96a3-e69b8435f005",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b6748071-993c-4610-9c36-1826af5751d5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9f8e782-e65a-4199-876c-4d57fbf8ef3c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f705c7d-0cd2-44ca-b977-6a9d8bd13800",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "76b78156-af33-4f20-a0e8-e8151bb94634",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "805b6ebf-ec88-47a9-a41b-65362dceec1a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96e7cc83-b4af-42a0-b044-66baca9072a5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1cbcd9bd-71b9-4f59-b1d7-71296b8fcd48",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f360ab4-f6c9-4e44-80a1-d46a6824bc9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ecf1fa3e-4ddb-401c-9c89-cf4ba5cbe296",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e7cdb29-661b-4438-9992-5a77213379ee",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2b9dd217-86cd-452b-b720-f9eddf054f37",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "993ad0b4-07fb-498c-8dc4-677b182a08bd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b2e52ef-571d-4a93-96f2-2150d3724f84",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9fe7c3b-d241-4231-a4fd-d7a280ce37d8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec089627-15db-4fc7-bdf4-7c5b896372d3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63f1c712-3e2f-4ffa-a7e3-b8c72aa0afc8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "335fd38b-e66d-4fe2-88ed-84be769ff2c8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d889c8e3-847f-476d-955d-a0afb2e29bcd",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
