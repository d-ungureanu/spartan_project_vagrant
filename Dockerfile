FROM python:latest
ADD app /app
ADD data /data
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app/main.py"]
