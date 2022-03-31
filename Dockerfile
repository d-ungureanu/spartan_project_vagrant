FROM python:latest
ADD database.config /database.config
ADD requirements.txt /requirements.txt
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app/main.py"]
