# Instructions

## Setting Virtual environment

[Why?](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

```
virtualenv venv
```

Every time you want to run or do anything with project, you need to activate 
virtual environment.

#### For Win (!PowerShell!)

run inside directory

```
$ venv\Scripts\activate.ps1
```

#### For Linux

```
$ source venv/bin/activate
```

## Install all Python packages needed

only Django so far, but there will be more soon.

```
$ pip install -r requirements
```

## Migrate database

In order to create/update database run

```
$ python manage.py migrate
```

## Run server

running the development server

```
$ python manage.py runserver
```