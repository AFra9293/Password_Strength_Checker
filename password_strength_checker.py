import re  # Import the regular expression library

# Function to check if the password length is at least 8 characters
def is_length_valid(password):
    return len(password) >= 8

# Function to check if the password contains at least one uppercase letter
def has_uppercase(password):
    return bool(re.search(r'[A-Z]', password))

# Function to check if the password contains at least one lowercase letter
def has_lowercase(password):
    return bool(re.search(r'[a-z]', password))

# Function to check if the password contains at least one digit
def has_digit(password):
    return bool(re.search(r'\d', password))

# Function to check if the password contains at least one special character
def has_special_char(password):
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

# Function to check the overall strength of the password
def check_password_strength(password):
    # Check each criterion and return appropriate feedback if it fails
    if not is_length_valid(password):
        return "Password must be at least 8 characters long."
    if not has_uppercase(password):
        return "Password must contain at least one uppercase letter."
    if not has_lowercase(password):
        return "Password must contain at least one lowercase letter."
    if not has_digit(password):
        return "Password must contain at least one digit."
    if not has_special_char(password):
        return "Password must contain at least one special character."
    # If all criteria are met, return that the password is strong
    return "Password is strong."

# Main block to allow user input and check the password strength
if __name__ == "__main__":
    # Prompt the user to enter a password
    password = input("Enter a password to check its strength: ")
    # Check the password strength and store the result
    result = check_password_strength(password)
    # Print the result
    print(result)
