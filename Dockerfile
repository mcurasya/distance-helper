FROM ubuntu:18.04
ADD . /
RUN apt-get update && apt-get  -y -q install python3 && apt-get -y -q install python3-pip && apt-get  -y -q install libreoffice-writer
RUN python3 -m pip install -r requirements.txt
CMD [ "python", "./main.py" ]