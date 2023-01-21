FROM python:latest

WORKDIR /

COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

EXPOSE 8081

ENV ENV_VAR='value'

CMD ["python", "main.py"]
