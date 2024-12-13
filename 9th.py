# Calculate total active and inactive medicines
total_medicines = len(df)
active_medicines = df['isActive'].sum()
inactive_medicines = total_medicines - active_medicines

# Calculate percentage distribution
active_percentage = round((active_medicines / total_medicines) * 100, 2)
inactive_percentage = round((inactive_medicines / total_medicines) * 100, 2)

# Output the result in comma-separated values
print(f"{active_percentage},{inactive_percentage}")
