FROM python:3.10-slim
WORKDIR /app
RUN pip install flask
COPY Datetime.py .
CMD ["python", "Datetime.py"]
