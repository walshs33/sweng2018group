# sweng2018group
repo for CS3013 group 25 project

# Git commands
Update your local copy:

git pull 

Add a file you want to commit changes to:

git add filename.txt

Commit changes to "stage":

git commit -m 'description of changes'

Push commits to the public repo:

git push

# Python stuff
https://learnpythonthehardway.org/book/ex0.html

https://www.codecademy.com/learn/learn-python

https://djangoforbeginners.com/

# Setup

pip install django mysqlclient

apt-get install mariadb

Create a new mysql user and database

Add mysql credentials to settings.py

To import db: mysql -u username -p dbname < db/db.sql

To add admin: python manage.py createsuperuser

To run server: python manage.py runserver

# ToDo
Login system for Principal Invetigator, Head of School, Faculty Office, HR

(Email/User and password)

Admin (for handover, they authenticate accounts etc)

Working form (stores data for now and identifies who currently needs to sign off on it)

Sign off page (for Head of School, Faculty Office, HR)

Email Notifications

Excel Spreadsheet
