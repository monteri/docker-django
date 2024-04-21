FROM python:3.8
ENV PYTHONUNBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
