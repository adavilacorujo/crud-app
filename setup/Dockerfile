FROM python:3.11-slim-bookworm

COPY --from=ghcr.io/ufoscout/docker-compose-wait:latest /wait /wait

ENV DBPORT="5432"
ENV DBNAME="notes"
ENV DBHOST="localhost"
ENV DBUSER="andres"
ENV DBPASSWORD="password"

WORKDIR /start-up
COPY . /start-up
RUN . ./venv/bin/activate
RUN pip --no-cache-dir install -r requirements.txt

CMD /wait && python main.py