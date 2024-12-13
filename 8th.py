# Count the frequency of each medicineName
medicine_frequency = df['medicineName'].value_counts()

# Get the 3rd most frequently prescribed medicineName
third_most_frequent = medicine_frequency.index[2]

# Output the result
print(third_most_frequent)
