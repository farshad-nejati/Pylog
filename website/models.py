from website import db
from sqlalchemy import Column, Integer, DateTime, func
from flask_login import  UserMixin
from werkzeug.security import  check_password_hash, generate_password_hash

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(33), nullable = False)
    password_hash = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(33), nullable = False)
    user_role = db.Column(db.String(33), nullable = False, default="student")
    status = db.Column(db.SMALLINT, default=0)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())
    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(255), nullable=False)
    image_url = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), onupdate=func.now())

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(33), nullable = False)

class PostCategory(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, primary_key=True)

print("this is model and run successfully")

