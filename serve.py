from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # Create a separate process for running stress_cpu.py
        subprocess.Popen(["python3", "stress_cpu.py"])
        return "CPU stress test started."
    else:
        # Return the private IP address of the EC2 instance
        return "Private IP address: " + socket.gethostbyname(socket.gethostname())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
