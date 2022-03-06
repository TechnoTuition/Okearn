from flask import Blueprint,render_template,request,flash,redirect,url_for,jsonify
from flask_login import current_user,login_required
from mysite import db
from werkzeug.utils import secure_filename
import os
from .utils import save_image
from mysite.home.models import User
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

@user.route('/profile-pic/',methods=['POST'])
@login_required
def profile_upload():
  f = request.files['picture']
  u = User.query.filter_by(id = current_user.id).first()
  save_im = save_image(f)
  print(save_im)
  u.image_file = save_im
  db.session.add(u)
  db.session.commit()
  
  return redirect(url_for("user.user_profile"))