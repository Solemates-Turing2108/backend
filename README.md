# backend

## set up instruction once you have python and pip (this is for our own reference. delete later)


### on the terminal: pull the repo and cd

#create a virtual environment\
$python3 -m venv .venv\
#activate that environment\
$source .venv/bin/activate\
#install flask\
$pip3 install flask\
#install sqlalchemy for database\
$pip3 install flask-sqlalchemy\


#create environment variables YOU NEED TO DO THESE TWO WHENEVE YOU EXIT THE TERMINAL\
$export FLASK_APP=application.py\
$export FLASK_ENV=development\


#setup database with python terminal\
$python3\
#import data from the application.py file\
$from application import db\


#create database. you will see data.db created if this is the first time\
$db.create_all()\

#if you don't do the two lines below and try to create user, you will get error: name 'User' is not defined - just have to import the User\
$from application import User\
$from application import Shoe\

#run flask server\
$flask run\

#exit python terminal \
$exit()\
