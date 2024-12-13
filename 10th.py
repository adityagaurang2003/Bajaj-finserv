# Define a function to check if a phone number is valid
def is_valid_mobile(number):
    # Remove any non-numeric prefix like '+91' or '91'
    if number.startswith('+91'):
        number = number[3:]
    elif number.startswith('91'):
        number = number[2:]
    
    # Check if the remaining number has exactly 10 digits and lies in the valid range
    if len(number) == 10 and number.isdigit() and 6000000000 <= int(number) <= 9999999999:
        return True
    return False

# Add a column isValidMobile
df['isValidMobile'] = df['phoneNumber'].apply(lambda x: is_valid_mobile(str(x)))

# Count the number of valid phone numbers
valid_phone_count = df['isValidMobile'].sum()

# Output the result
print(valid_phone_count)
