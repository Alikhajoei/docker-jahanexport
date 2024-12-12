FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip3 install --upgrade pip  && pip3 install -r requirements.txt 

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
