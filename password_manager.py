# password_manager.py
import secrets
#import random
import string
import install_db
import config_db
#import connect_db


# Install and start MariaDB
install_db.install_mariadb()

# Set the environment variables
config_db.set_env_variables()

# Insert a password into the database
# connect_db.insert_password('mypassword')


# Create a cryptographically secure RNG
rng = secrets.SystemRandom()

# Characters list
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation


# Set the length of the password
pwd_length = int(input("Please enter a password length (8-16): "))

while not 8 <= pwd_length <= 16:
    pwd_length = int(input("Please enter a valid password length (8-16): "))

# Generate a password according to conditions
for p in range(100):
    pwd = "".join(rng.choice(letters + digits + special_chars) for _ in range(pwd_length))

    if (sum(char.isdigit() for char in pwd) >= 2 and \
        sum(char.islower() for char in pwd) >= 2 and \
        sum(char.isupper() for char in pwd) >= 2 and \
        any(not char.isalnum() for char in pwd)):
        
        break

print(pwd)
