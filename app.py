# app.py
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root (home) page
@app.route('/')
def hello_world():
    return 'This is a Test Web Page on Azure Web Services\nBy Akash Tomar !'

# Run the app if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
