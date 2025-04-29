FROM python:alpine
WORKDIR /opt/flask
COPY ./app /opt/flask
RUN pip install -r requirements.txt
CMD ["python","app.py"]
