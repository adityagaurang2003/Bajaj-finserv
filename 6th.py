# Define age group categorization
def categorize_age(age):
    if pd.isnull(age):
        return None
    elif age <= 12:
        return 'Child'
    elif 13 <= age <= 19:
        return 'Teen'
    elif 20 <= age <= 59:
        return 'Adult'
    else:
        return 'Senior'

# Add ageGroup column
df['ageGroup'] = df['age'].apply(categorize_age)

# Calculate the count of Adults
adult_count = (df['ageGroup'] == 'Adult').sum()

# Output the result
print(adult_count)
