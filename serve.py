import webview
import subprocess
import os
import time

# Function to start your web server
def start_server():
    process = subprocess.Popen(["yarn", "start"], cwd=os.path.join(os.getcwd()), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return process

# Start the server
server_process = start_server()

# Wait for the server to start
time.sleep(5)  # Adjust the sleep time as necessary

# URL to your locally running web application
url = "http://localhost:3000"

# Create and display a Pywebview window
webview.create_window('Sahara KA', url)
webview.start()

# Terminate the server when the Pywebview window is closed
server_process.terminate()