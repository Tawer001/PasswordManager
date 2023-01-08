# install_db.py
import subprocess


def install_mariadb():
    # Run the MariaDB installer
    subprocess.check_call(['msiexec', '/i', 'Database/Installation/mariadb-10.11.1-winx64.msi'])

    # Start the MariaDB service
    subprocess.check_call(['net', 'start', 'mariadb'])
