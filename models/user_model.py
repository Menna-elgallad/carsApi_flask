from models import BaseModelMixin
from ext import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(BaseModelMixin):
    __tablename__ = 'users'
    username = db.Column(db.String(20),unique=True,nullable=False)
    password = db.Column(db.String(120),nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(80))
    
    def __init__(self, username, password, name, email):
        self.username = username
        self.password = generate_password_hash(password)
        self.name = name
        self.email = email
    def __repr__(self):
        return f'<User {self.username}>'
    
    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)    