from flask import Flask, Request, Response
from app import app  # Assuming your Flask app is defined in app.py

# Create a WSGI application
server = Flask(__name__)

# Define the serverless function
@server.route('/api', methods=['GET', 'POST'])
def handler(req: Request) -> Response:
    return app(req.environ, lambda status, headers: None)

# Run the serverless function
if __name__ == '__main__':
    from werkzeug.serving import run_simple
    run_simple('localhost', 5000, server)