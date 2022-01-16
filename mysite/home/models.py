from mysite import db, login_manager,app
from datetime import datetime
from flask_login import UserMixin
from itsdangerous import JSONWebSignatureSerializer as Serializer
from mysite.blog.models import Blog,Like

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
class User(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String(20),unique=False,nullable=False)
    lastname = db.Column(db.String(20),unique=False,nullable=False)
    email = db.Column(db.String(25),unique=True,nullable=False)
    password = db.Column(db.String(20),unique=False,nullable=False)
    image_file = db.Column(db.String(50),nullable=False,default="default.png")
    user_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    posts = db.relationship('Blog',backref='users',lazy=True)
    likes = db.relationship('Like',backref='users',lazy=True)
    
    def get_reset_token(self,expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'])
        return s.dumps({'user_id': self.id}).decode('utf-8')
        
       
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
        