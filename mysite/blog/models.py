from mysite import db
#from mysite.home.models import User
from datetime import datetime

class Blog(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  title = db.Column(db.String(100),unique=False,nullable=False)
  slug = db.Column(db.String(20),unique=False,nullable=False)
  body = db.Column(db.String(1000),unique=False,nullable=False)
  post_created = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
  post_image = db.Column(db.String(50),unique=False,nullable=True)
  views = db.Column(db.Integer,nullable=True,default=0)
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)
  like =  db.relationship('Like',backref='blog',lazy=True)
    
class Like(db.Model):
  id = db.Column(db.Integer,primary_key=True)
  user_id = db.Column(db.Integer,db.ForeignKey('user.id',ondelete="CASCADE"),nullable=False)
  post_id = db.Column(db.Integer,db.ForeignKey('blog.id',ondelete="CASCADE"),nullable=False)

