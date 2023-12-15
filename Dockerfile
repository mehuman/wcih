FROM python:3

ADD . /app
WORKDIR /app
RUN apt-get update && apt-get install -y ghostscript python3-tk ffmpeg libsm6 libxext6 libgl1-mesa-dev libglib2.0-0

RUN pip install -r requirements.txt

ENTRYPOINT python camtest.py
