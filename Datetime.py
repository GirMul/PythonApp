from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Date Time App</title>
</head>
<body style="font-family: Arial; text-align: center; margin-top: 50px;">
    <h2>Current Date & Time</h2>
    <p>{{ time }}</p>
    <form method="get">
        <button type="submit">Refresh Time</button>
    </form>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, time=datetime.now())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

