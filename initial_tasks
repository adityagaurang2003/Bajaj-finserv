import json
import pandas as pd

# Load the JSON file
file_path = 'C:\Users\Dell\Downloads\DataEngineeringQ2.json'
with open(file_path, 'r') as file:
    data = json.load(file)

# Parse and normalize JSON data
# Extract patientDetails and medicines from consultationData
records = []
for entry in data:
    patient_details = entry.get('patientDetails', {})
    medicines = entry.get('consultationData', {}).get('medicines', [])
    for med in medicines:
        records.append({
            'appointmentId': entry.get('appointmentId', ''),
            'patientId': patient_details.get('_id', ''),
            'firstName': patient_details.get('firstName', ''),
            'lastName': patient_details.get('lastName', ''),
            'gender': patient_details.get('gender', ''),
            'birthDate': patient_details.get('birthDate', ''),
            'medicineId': med.get('medicineId', ''),
            'medicineName': med.get('medicineName', ''),
            'frequency': med.get('frequency', ''),
            'duration': med.get('duration', ''),
            'durationIn': med.get('durationIn', ''),
            'instruction': med.get('instruction', ''),
            'isActive': med.get('isActive', '')
        })

# Convert to DataFrame
df = pd.DataFrame(records)
df.head()
# Data Transformation and Cleaning

# Convert 'birthDate' to a datetime object for easier age calculation
df['birthDate'] = pd.to_datetime(df['birthDate'], errors='coerce')

# Add a derived column for age (assuming current year is 2024)
df['age'] = df['birthDate'].apply(lambda x: 2024 - x.year if pd.notnull(x) else None)

# Ensure 'duration' is numeric
df['duration'] = pd.to_numeric(df['duration'], errors='coerce')

# Aggregation: Count of active medicines by patient
active_meds_by_patient = df[df['isActive']].groupby('patientId')['medicineName'].count().reset_index()
active_meds_by_patient.columns = ['patientId', 'activeMedicinesCount']

# Aggregation: Average duration of medicines by gender
avg_duration_by_gender = df.groupby('gender')['duration'].mean().reset_index()
avg_duration_by_gender.columns = ['gender', 'avgDuration']

# Aggregation: Most frequently prescribed medicines
most_frequent_medicines = df['medicineName'].value_counts().reset_index()
most_frequent_medicines.columns = ['medicineName', 'count']

# Display transformed data and key aggregations
df_cleaned = df[['patientId', 'firstName', 'gender', 'age', 'medicineName', 'isActive', 'duration']]
active_meds_by_patient, avg_duration_by_gender, most_frequent_medicines.head()
# Data Validation
# Check for missing or inconsistent data in critical fields

validation_summary = {
    "missing_firstName": df['firstName'].isnull().sum(),
    "missing_gender": df['gender'].isnull().sum(),
    "missing_birthDate": df['birthDate'].isnull().sum(),
    "invalid_duration": df['duration'].isnull().sum(),
    "invalid_medicineName": df['medicineName'].isnull().sum(),
    "active_medicines_without_duration": df[df['isActive'] & df['duration'].isnull()].shape[0]
}

# Insights: Unique medicines prescribed by active status
active_medicines_insights = df[df['isActive']]['medicineName'].value_counts().reset_index()
active_medicines_insights.columns = ['medicineName', 'activeCount']

inactive_medicines_insights = df[~df['isActive']]['medicineName'].value_counts().reset_index()
inactive_medicines_insights.columns = ['medicineName', 'inactiveCount']

validation_summary, active_medicines_insights.head(), inactive_medicines_insights.head()
