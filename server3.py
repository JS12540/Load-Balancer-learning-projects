# server3.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Server 3!'

if __name__ == '__main__':
    app.run(port=5003)
