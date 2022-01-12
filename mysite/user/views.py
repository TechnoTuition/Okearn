from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import current_user,login_required

user = Blueprint('user',__name__)

@user.route('/')
@login_required
def index():
  print(current_user.posts)
  return render_template("user/index.html",user=current_user)

#profile

@user.route('/profile/',methods=["GET","POST"])
@login_required
def user_profile():
  return render_template("user/profile.html")