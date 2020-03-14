# Instagram Clone
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Description
This a web application built using Python, Django and Postgresql.The app is a clone  of the Awwwards web app, you can view posted projects that have been posted with the necessary details. As a user you can post project to be rated and reviewed by other users. As a user you can also rate and review other users' projects, you can also search for a specific projects, view your own and other users' projects. As well as view your profile page


## Author

Samuel Aronda


## DB diagram



# Installation

## Clone
    
```bash
    git clone https://github.com/arondasamuel123/AwwwardsClone.git
    
```
##  Create virtual environment
```bash
    python3.6 -m venv --without-pip virtual
    
```
## Activate virtual and install requirements.txt
```bash
   $ source virtual/bin/activate
   $ pip install - requirements.txt
    
```
## Run initial migration
```bash
   $ python3.6 manage.py makemigrations awards
   $ python3.6 manage.py migrate
    
```


## Run app
```bash
   $ python3 manage.py runserver
    
```

## Test class

```bash
    $ python3 manage.py test
```
## Known Bugs


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## Technologies Used
    Python Shell
    Python 3.6
    Django
    Bootstrap Materialize
    HTML
    CSS
    PostgreSQL
    Django Rest Framework




