FROM python:latest

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY vendor/ffmpeg vendor/ffmpeg
COPY *.py .

EXPOSE 7080

ENTRYPOINT [ "python3", "index.py" ]