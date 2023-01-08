# config_db.py
import utils

os = utils.import_module('os')


# Set multiple environment variables at once
os.environ.update({
    'DB_HOST': 'localhost',
    'DB_USER': 'myuser',
    'DB_PASSWORD': 'mypassword',
    'DB_DATABASE': 'pwd_mngr'
})
