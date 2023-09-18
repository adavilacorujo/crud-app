FROM python:3.11-slim-bookworm

ENV DBPORT="5432"
ENV DBNAME="notes"
ENV DBHOST="172.17.0.2"
ENV DBUSER="andres"
ENV DBPASSWORD="password"

WORKDIR /app
COPY . /app
RUN . ./venv/bin/activate
RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "-t", "10000", "-w", "4","app:app"]