FROM python:3.8-slim-buster
WORKDIR /trace
ENV FLASK_APP app.py
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY app.py .
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]
