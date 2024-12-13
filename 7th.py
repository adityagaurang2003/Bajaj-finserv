# Group by appointmentId and count the number of medicines for each appointment
medicines_per_appointment = df.groupby('appointmentId')['medicineId'].count()

# Calculate the average number of medicines
average_medicines = round(medicines_per_appointment.mean(), 2)

# Output the result
print(average_medicines)
