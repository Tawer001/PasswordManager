# config_db.py
import os

os.environ['DB_HOST']: 'localhost'

# Set multiple environment variables at once
os.environ.update({
    'DB_USER': 'myuser',
    'DB_PASSWORD': 'mypassword',
    'DB_DATABASE': 'pwd_mngr'
})
