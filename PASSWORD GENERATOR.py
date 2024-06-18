import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage
password = generate_password(16)
print(f"Generated password: {password}")
