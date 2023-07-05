# Python and SQLite inside Docker

This Repository is tutorial on how to make a python script interact with an MySQL Database inside a Docker Container

- [SQLite](#sqlite)
- [MySQL](#mysql)
- [Python](#python)

## SQLite

To create a new SQLite db inside a docker container run the `Dockerfile` inside the `SQLite` directory

```bash
docker build -t my-sqlite-container .
docker run -p 8080:8080 --name my-sqlite-container my-sqlite-container
```

To create the Database use the shell script `create_db.sh`. It will create a new database named `names.db`

## MySQL

An SQLite DB is just a `.db` file and not a server. To make a Python script running on a separate Docker container interact with a DB we need the DB container to be persiste (i.e. a client / server type of DB)

We will be using MySQL for this purpose

The process of building the DB is quite similar but we need to set additional Environment variables to set up our DB and make the container visible to the other running the python script


## Python 