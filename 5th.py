# Impute missing values in the 'gender' column with its mode
mode_gender = df['gender'].mode()[0]
df['gender'] = df['gender'].replace('', mode_gender)

# Calculate the percentage of females in the gender column
total_count = len(df)
female_count = (df['gender'] == 'F').sum()
female_percentage = round((female_count / total_count) * 100, 2)

# Output the result
print(female_percentage)
