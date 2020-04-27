FROM ubuntu:18.04
ADD . /
RUN apt-get update && apt-get install python3 && apt-get install libreoffice libreoffice-writer
RUN pip3 install -r requirements.txt
CMD [ "python", "./main.py" ]