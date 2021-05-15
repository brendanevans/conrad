FROM python:3.9

RUN mkdir /conrad
WORKDIR /conrad

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

ENV TZ=Australia/Brisbane
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

CMD ["python","main.py"]