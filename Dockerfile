FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m pip install --upgrade pip

CMD ["python", "app.py"]
