## Env
- Python: 3.10.10
- Flask: 2.3.2
- MySQL: 8.0.33
- Gunicorn(AP Server)

## Get Started
```bash
$ docker compose build
$ docker compose up
$ curl http://localhost:8000/api/hello
```

### Package dependency management
Use poetry instead of requirements.txt.
```bash
$ poetry add xxx
$ poetry remove xxx

# only prod
$ poetry install --no-dev
```

## Create DB
```bash
$ mysql -h 127.0.0.1 -u root -P 3666 -p flask_db
$ mysql> create database flask_db;
# for db
$ mysql> create database flask_db_test;
$ mysql> ALTER USER root IDENTIFIED WITH mysql_native_password BY 'flask-db';
```

## Shell
```bash
$ flask shell
```

```ssh
$ docker exec -it flask-backend /bin/bash
```

## Check Routing
```bash
>>> app.url_map
```

```bash
# only-first
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade

# rollback
flask db downgrade
```

## Debug
```bash
breakpoint()
```

## Use linter and formatter
```bash
# Use linter
$ flake8 .

# Use formater
$ isort .
$ black .
```
