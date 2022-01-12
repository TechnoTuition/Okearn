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
  user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)