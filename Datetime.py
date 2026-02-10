from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Date Time App</title>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 50px;">
        <h2>Current Date & Time</h2>
        <p>{current_time}</p>
        <form method="get">
            <button type="submit">Refresh Time</button>
        </form>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
