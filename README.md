# Herrera-Pon-An-Reyes-OTech

Steps to run the app:
1. open command prompt
2. cd <location address of file>
3. install the following requirements by typing:

pip install flask

python
import flask

pip install flask-wtf

python
import secrets
secrets.token_hex(16)
exit()

pip install flask-sqlalchemy

python
from CRUD import db
from CRUD.models import User, Post
db.create_all()
exit()

pip install flask-bcrypt

python
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()
bcrypt.generate_password_hash('testing')
bcrypt.generate_password_hash('testing').decode('utf-8')
bcrypt.generate_password_hash('testing').decode('utf-8')
hashed_pw = bcrypt.generate_password_hash('testing').decode('utf-8')
exit()

pip install flask-login
pip install flask-cors
pip install Pillow

set FLASK_APP=run.py
python run.py

To run using Docker:
docker-composer up -d --build
and browse to localhost:8000


Functionalities:
- CRUD functions for:
	1. User
	2. Reservations
- Read function for:
	1. History
	2. Menu
