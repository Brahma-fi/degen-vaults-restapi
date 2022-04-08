FROM python:3.8

ADD . .

RUN  pip3 install -r requirements.txt

EXPOSE 5000

ENV PATH /env/bin:$PATH

RUN apt-get update

RUN apt-get install -y gunicorn

CMD ["gunicorn","-w 4", "-b 0.0.0.0:5000", "src.app:app" ]