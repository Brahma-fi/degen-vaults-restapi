FROM python:3.8

ADD . .

RUN  pip3 install -r requirements.txt

EXPOSE 5000

CMD [ "python3", "src/app.py" ]