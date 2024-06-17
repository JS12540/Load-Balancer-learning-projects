# load_balancer.py
from flask import Flask, request, Response
import requests

app = Flask(__name__)

# List of backend servers
servers = [
    'http://127.0.0.1:5001',
    'http://127.0.0.1:5002',
    'http://127.0.0.1:5003'
]

# Variable to keep track of the current server index
current_server_index = 0

@app.route('/')
def load_balance():
    global current_server_index
    # Get the URL of the current server to forward the request
    server_url = servers[current_server_index]
    
    # Update the current server index for the next request (round-robin)
    current_server_index = (current_server_index + 1) % len(servers)
    
    try:
        # Forward the request to the selected server
        response = requests.get(server_url)
        
        # Create a response object with the response from the server
        return Response(response.content, status=response.status_code, headers=dict(response.headers))
    except requests.exceptions.RequestException as e:
        # If the request to the server fails, return an error response
        return f'Error: {e}', 503

if __name__ == '__main__':
    # Run the load balancer on port 5000
    app.run(port=5000)
