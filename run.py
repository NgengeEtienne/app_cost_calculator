import os
import subprocess
import webbrowser
import time

def start_server_and_open_browser():
    project_dir = "app_cost_calculator"

    #os.chdir(project_dir)

    # Run migrations, seed the database, and start the Django server
    subprocess.Popen('cmd.exe /K "python manage.py makemigrations & python manage.py migrate & python manage.py seed & python manage.py runserver 22000"', shell=True)

    # Wait for the server to start (adjust the sleep time as needed)
    time.sleep(5)  # Adjust the sleep time if necessary

    # Open browser
    webbrowser.open('http://127.0.0.1:22000/')

if __name__ == "__main__":
    start_server_and_open_browser()
