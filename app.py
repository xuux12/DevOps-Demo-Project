
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def hello_world():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello World! 👋</h1>
        <p>My Flask application is running.</p>
    </body>
    </html>
    """

# Endpoint 2: API
@app.route("/api/hello")
def api_hello():
    return jsonify({
        "message": "Hello World!",
        "status": "success"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


