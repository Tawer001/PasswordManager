import secrets
import string

# Set the length of the password
pwd_length = int(input("Please enter a password length (8-16): "))

while not 8 <= pwd_length <= 16:
    pwd_length = int(input("Please enter a valid password length (8-16): "))

# Create a cryptographically secure RNG
rng = secrets.SystemRandom()

# Characters list
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

# Generate a password according to conditions
while True:
    pwd = ''.join(rng.choice(letters + digits + special_chars) for _ in range(pwd_length))
    
    if (sum(char.isdigit() for char in pwd) >= 2 and \
        sum(char.islower() for char in pwd) >= 2 and \
        sum(char.isupper() for char in pwd) >= 2 and \
        any(not char.isalnum() for char in pwd)):
        
        break

print(pwd)
