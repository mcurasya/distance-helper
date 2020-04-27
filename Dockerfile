FROM ubuntu:18.04
ADD . /
RUN apt-get update && apt-get  -y -q install python3 && apt-get  -y -q install libreoffice-writer
RUN pip3 install -r requirements.txt
CMD [ "python", "./main.py" ]