from flask import Blueprint,render_template,request,flash,redirect,url_for,jsonify
from flask_login import current_user,login_required

user = Blueprint('user',__name__)

@user.route('/')
@login_required
def index():
  views = 0
  for post in current_user.posts:
    views = views + post.views
  like = 0
  for post in current_user.posts:
    like = like+ len(post.like)
  print(like)
  return render_template("user/index.html",user=current_user,views=views,like=like)

@user.get('/userdata/')
@login_required
def userdata():
  views = 0
  for post in current_user.posts:
    views = views + post.views
  like = 0
  for post in current_user.posts:
    like = like+ len(post.like)
  return jsonify({'views': views})
#profile

@user.route('/profile/',methods=["GET","POST"])
@login_required
def user_profile():
  return render_template("user/profile.html")