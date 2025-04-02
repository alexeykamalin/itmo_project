FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt
RUN pip install bcrypt
RUN pip install fastapi
RUN pip install rabbitmq
RUN pip install postgres
RUN pip install SQLAlchemy

EXPOSE 8080

# COPY ./ /app

CMD ["python", "main.py"]