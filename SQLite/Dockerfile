FROM ubuntu:latest


RUN apt-get update && apt-get install -y sqlite3 sudo

COPY . .

RUN chmod +x ./create_db.sh
RUN ./create_db.sh


EXPOSE 8080

CMD ["sqlite3", "name.db"]