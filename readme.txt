Run server with
> python manage.py runserver 37.191.215.88:8000

Update the database after making changes to model
> python manage.py schemamigration Norskkurs --auto
> python manage.py migrate Norskkurs


How to set up guide:
https://www.digitalocean.com/community/articles/how-to-install-and-configure-django-with-postgres-nginx-and-gunicorn

DATABASE COMMANDS:

database console:
sudo su - postgres
psql

connect to database:
\c nkdb

list all tables:
\dt


If you dont mind feeling dirty, how to delete and recreate DB:
sudo su - postgres
dropdb nkdb
createdb nkdb
psql
GRANT ALL PRIVILEGES ON DATABASE nkdb TO myuser;
\q
exit

delete migrations and then:
python manage.py syncdb --migrate

Fake it till you make it:
python manage.py migrate Norskkurs --fake
