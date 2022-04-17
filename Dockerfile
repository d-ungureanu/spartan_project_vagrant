FROM python:latest
ADD requirements.txt /requirements.txt
ADD app /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "/app/main.py"]
