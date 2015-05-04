FROM python
MAINTAINER sergiobuj

ADD requirements.txt /

RUN pip3 install -r requirements.txt

ADD . /

EXPOSE 5000

ENTRYPOINT ["python", "server.py"]
