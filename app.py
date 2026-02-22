from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
    # This returns the required "Hello Cloud" message
    return "<h1>Hello Muhammad Jalal</h1><p>Running inside a Docker Container!</p>"

if __name__ == "__main__":
    # Standard Flask port for the assignment
    app.run(host='0.0.0.0', port=5000)