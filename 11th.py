# Group by patientId to count the number of medicines prescribed per patient
medicines_count_per_patient = df.groupby('patientId')['medicineName'].count().reset_index()
medicines_count_per_patient.columns = ['patientId', 'medicinesCount']

# Merge the medicines count with the patient age
df_patient_age = df[['patientId', 'age']].drop_duplicates()
merged_data = pd.merge(medicines_count_per_patient, df_patient_age, on='patientId')

# Calculate the Pearson correlation
correlation = round(merged_data['medicinesCount'].corr(merged_data['age']), 2)

# Output the result
print(correlation)
