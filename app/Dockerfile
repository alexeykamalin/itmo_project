FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install -r /app/requirements.txt

EXPOSE 8080

# COPY ./ /app

CMD ["python", "api.py"]