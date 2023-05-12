# HR-system-BE

In this document you will find the requirements and steps in order to install the API on your local machines. Please if you're facing any issues do not hesitate to ask @AhmadSaadeh

## Requirements

- Python >= 3.9
- MySQL
<!-- please note that the following are in the requirements.text so dont install them now -->
- Django == 4.2.1
- Django REST Framework == 3.14.0

## Prerequisities

First we need to setup python dev enivornment as well as MySQL server, to do so, we need to install the following libraries on Ubuntu

```
sudo apt-get update
sudo apt-get install python-pip python-dev mysql-server libmysqlclient-dev
```

You’ll be asked for the administrative password you set for MySQL during installation, make sure the password is the same as in the Django project settings (QWEqwe!1).


### Setup MySQL User and Grant Privileges

We can start by logging into an interactive session with our database software by typing the following (the command is the same regardless of which database software you are using):

```
mysql -u root -p
```

You will be prompted for the administrative password you selected during installation.

First, we will create a database for our Django project. Each project should have its own isolated database for security reasons. We will call our database `hr_db`. We’ll set the default type for the database to UTF-8, which is what Django expects:

```
CREATE DATABASE hr_db CHARACTER SET UTF8;
```

Now, all we need to do is give our database user access rights to the database we created:

```
GRANT ALL PRIVILEGES ON hr_db.* TO root@localhost;
```

Flush the changes so that they will be available during the current session:

```
FLUSH PRIVILEGES;
```

That is it, now exit MySQL shell by typing:

```
exit



### Install Requirements within a Virtual Environment

Now that our database is set up, we can install Django. For better flexibility, we will install Django and all of its dependencies within a Python virtual environment.
You can get the `virtualenv` package that allows you to create these environments by typing:

```
sudo pip install virtualenv
```

In the project directory, create the virtual environment using python 3.9 please check if the path to the python version you are going to use matches the one below :

```
virtualenv -p /usr/bin/python3.9 venv
```

Now you will have a folder called `venv` that is your virtual environment, to start it, you should type:

```
source venv/bin/activate
```

Now that you have activated the virtual environment, you need to install the requirements, by typing:

```
pip install -r requirements.txt


## Running The Project

First, you need to migrate the database, that is done via django script:

```
python manage.py migrate
```

If you have no migrations file, you should create ones first:

```
python manage.py makemigrations
```

After that, you can run the project by typing:

```
python manage.py runserver
```

