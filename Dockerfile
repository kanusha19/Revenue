FROM python:3.8

RUN pip install --upgrade pip

WORKDIR /app

COPY actions /app/actions

COPY config.yml /app/config.yml

COPY data /app/data

COPY models /app/models

COPY endpoints.yml /app/endpoints.yml

COPY domain.yml /app/domain.yml

COPY credential.yml /app/credential.yml

COPY train.sh /app/

COPY requirements.txt ./


RUN pip install -r requirements.txt

RUN pip install duckling

RUN chmod 755 train.sh

CMD sh train.sh