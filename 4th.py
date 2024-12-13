def missing_percentage(column):
    total = len(df)
    missing = df[column].apply(lambda x: x == '' or pd.isnull(x)).sum()
    return round((missing / total) * 100, 2)

# Calculate for specified columns
missing_firstName_pct = missing_percentage('firstName')
missing_lastName_pct = missing_percentage('lastName')
missing_birthDate_pct = missing_percentage('birthDate')

# Combine results into comma-separated string
missing_values_percentage = f"{missing_firstName_pct},{missing_lastName_pct},{missing_birthDate_pct}"
missing_values_percentage
