
FROM python:3.10-slim

# Install tkinter dependency
RUN apt-get update && apt-get install -y python3-tk && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY BallGame.py .

CMD ["python", "BallGame.py"]
