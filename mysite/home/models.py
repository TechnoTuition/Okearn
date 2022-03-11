from mysite import db, login_manager,app
from datetime import datetime
from flask_login import UserMixin
from mysite.blog.models import Blog,Like

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

user_fallow = db.Table('user_fallow',
db.Column('id', db.Integer,primary_key=True),
db.Column('user_id',db.Integer,db.ForeignKey('user.id', ondelete='CASCADE')),
db.Column('fallow_id',db.Integer,db.ForeignKey('fallow.id', ondelete='CASCADE'))
)
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(20),unique=False,nullable=True)
    lastname = db.Column(db.String(20),unique=False,nullable=True)
    email = db.Column(db.String(25),unique=True,nullable=False)
    is_admin = db.Column(db.Boolean,default=False,nullable=True)
    is_active = db.Column(db.Boolean,default=False,nullable=False)
    password = db.Column(db.String(20),unique=False,nullable=False)
    image_file = db.Column(db.String(50),nullable=False,default="default.png")
    user_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    posts = db.relationship('Blog',backref='users',lazy=True,cascade='all, delete-orphan',single_parent=True)
    likes = db.relationship('Like',backref='users',lazy=True,passive_deletes=True)
    fallowing = db.relationship('Fallow',secondary=user_fallow,backref='fallowers',lazy=True,passive_deletes=True)
    
class Fallow(db.Model):
  id = db.Column(db.Integer,primary_key=True)
