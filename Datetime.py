from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Python Flask Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f6f8;
            text-align: center;
            padding-top: 80px;
        }
        h1 {
            color: #333;
        }
        button {
            padding: 12px 25px;
            font-size: 16px;
            cursor: pointer;
            background-color: #0073e6;
            color: white;
            border: none;
            border-radius: 5px;
        }
        button:hover {
            background-color: #005bb5;
        }
        .time {
            margin-top: 20px;
            font-size: 20px;
            color: #444;
        }
    </style>
</head>
<body>
    <h1>🚀 Python Flask Website</h1>
    <p>This page is running inside Docker on AWS EC2</p>

    <form method="get">
        <button type="submit">Show Current Date & Time</button>
    </form>

    {% if current_time %}
        <div class="time">
            ⏰ Current Time: <b>{{ current_time }}</b>
        </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template_string(HTML_PAGE, current_time=current_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
