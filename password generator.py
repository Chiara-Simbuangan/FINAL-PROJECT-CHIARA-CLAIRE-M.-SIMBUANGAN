import random
import string

def generate_password(length=12):
    """Generates a random password with the specified length."""
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
password_length = int(input("Enter the desired password length: "))
password = generate_password(password_length)
print(f"Generated password: {password}")
