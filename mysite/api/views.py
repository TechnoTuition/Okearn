from flask import Blueprint,jsonify
from mysite.home.models import User
from mysite.blog.models import Blog
from .serializer import blog_schema,blogs_schema
api = Blueprint('api',__name__)

@api.get('/')
def api_docs():
  return jsonify({"api": "documentaion"})

@api.get('/users/')
def all_user():
  users = User.query.all()
  print(users)
  data = []
  for user in users:
    users_data = {}
    users_data['id'] = user.id
    users_data['firstname'] = user.firstname
    users_data['lastname'] = user.lastname
    users_data['email'] = user.email
    users_data['fallowing'] = len(user.fallowing)
    users_data['posts'] = len(user.posts)
    data.append(users_data)
  print(data)
  return jsonify(data)


@api.route('/user/<id>/',methods=["GET","POST"])
def single_user(id):
  users = User.query.all()
  alldata = []
  for user in users:
    data = dict(id = user.id,firstname=user.firstname,lastname=user.lastname,email=user.email,image_file=user.image_file)
    alldata.append(data)
  print(alldata[int(id)])
  return jsonify(alldata[int(id)])
  
# create serializer class
@api.get('/post')
def all_post():
  post = Blog.query.all()
  print(post)
  data = blogs_schema.dump(post)
  print(data)
  return jsonify(data)
