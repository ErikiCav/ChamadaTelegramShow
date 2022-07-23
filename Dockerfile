FROM ubuntu:focal
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt upgrade -y
RUN apt install ffmpeg -y
RUN apt install git curl python3-pip ffmpeg -y
RUN apt install curl -y
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN pip3 install -U pip
RUN pip3 install -U git+https://github.com/pyrogram/pyrogram@master
RUN apt-get install -y nodejs
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
RUN pip3 install -U -r requirements.txt
CMD ["python3","setup.py"]