from flask import Blueprint,render_template,request,flash,redirect,url_for,session,jsonify
import sqlalchemy
from .forms import RegisterForm,LoginForm,EmailVerificationForm
from .models import User,Fallow
from mysite.blog.models import Blog
from mysite import bcrypt,db,mail,final,socketio
from flask_login import login_user,current_user,login_required,logout_user
from .utils import email_verification,reset_pass_mail
import json
import jwt
from os import environ
from flask_socketio import send
import datetime
home = Blueprint('home',__name__)

@home.route('/')
def index():
  post = Blog.query.all()
  for i in post:
    print(i.users.image_file)
  popularPost = Blog.query.filter(Blog.views>2).all()
  return render_template("home/index.html",posts=post,popularPost=popularPost)
# register form 
@home.route('/register/',methods=['GET','POST'])
def user_register():
  if current_user.is_authenticated and current_user.is_active == True:
    return redirect(url_for("user.index"))
  if request.method == "POST":
    form = RegisterForm()
    if form.validate_on_submit():
      print(form.firstname.data,form.lastname.data,form.email.data,form.password.data)
      user = User.query.filter_by(email=form.email.data).first()
      if user:
        flash("Email Account Already Exist","danger")
        return redirect(url_for("home.user_login"))
      else:
        pass_hash = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_user = User(firstname=form.firstname.data,lastname= form.lastname.data,email=form.email.data,password=pass_hash,is_active=False)
        new_fallow = Fallow()
        db.session.add(new_fallow)
        db.session.add(new_user)
        db.session.commit()
        token = jwt.encode({"email": new_user.email,"exp": datetime.datetime.utcnow()+datetime.timedelta(seconds=120)},environ['SECRET_KEY'],algorithm='HS256')
        url = f"{url_for('home.email_verify',token=token,_external=True)}"
        email_verification(url,form.email.data)
        flash("Please activet your check your email  ")
        return redirect("/login")
  else:
    form = RegisterForm()
  return render_template('home/signup.html',form=form)


# login form 
@home.route('/login/',methods=["GET","POST"])
def user_login():
  if current_user.is_authenticated and current_user.is_active == True:
    return redirect(url_for("user.index"))
  if request.method == "POST":
    form = LoginForm()
    if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      
      if user and bcrypt.check_password_hash(user.password,form.password.data) and user. is_active == True:
        login_user(user,remember=True)
        return redirect(url_for("home.index"))
      else:
        flash("email or password dose not match ","danger")
        return redirect(url_for("home.user_login"))
  else:
    form = LoginForm()
  return render_template('home/login.html',form=form)
# logout user
@home.route('/logout/',methods=["GET","POST"])
def logout():
  logout_user()
  return redirect(url_for("home.user_login"))


# email_verification
@home.route('/email_verification/<token>/',methods=["GET","POST"])
def email_verify(token):
  print(token)
  try:
    token = jwt.decode(token,environ['SECRET_KEY'],algorithms='HS256')
    user = User.query.filter_by(email=token['email']).first()
    user.is_active = True
    db.session.add(user)
    db.session.commit()
  except jwt.ExpiredSignatureError:
    flash("token expired")
    return redirect("/register")
  except jwt.InvalidSignatureError:
    flash('envalid url')
    return redirect("/register")
  return redirect("/login")

@home.route('/forgotpassword/',methods=["GET","POST"])
def forget_password():
  if request.method == "POST":
    email = request.form.get("email")
    u = User.query.filter_by(email=email).first()

    if u:
      flash("Please check your email to reset your password ")
      token = jwt.encode({"email": u.email ,"exp": datetime.datetime.utcnow()+datetime.timedelta(seconds=60)},environ['SECRET_KEY'],algorithm="HS256")
      URL = f"{url_for('home.new_password',token=token,_external=True)}"
      reset_pass_mail(URL,u.email)
      with open("url.txt","w") as f:
        f.write(URL)
      return redirect('/forgotpassword/')
    else:
      flash("email accont not found")
      return redirect("/forgotpassword")
  return render_template("home/forgotpassword.html")


@home.route('/newpassword/<token>/',methods=["GET","POST"])
def new_password(token):
  try:
    u = jwt.decode(token, environ['SECRET_KEY'],algorithms="HS256")
    
    if request.method == "POST":
      email = User.query.filter_by(email=u['email']).first()
      pass_hash = bcrypt.generate_password_hash(request.form.get("pass"))
      email.password = pass_hash
      db.session.add(email)
      db.session.commit()
      flash("your password has been reset")
      return redirect(url_for('home.user_login'))
  except jwt.ExpiredSignatureError:
    flash("token expired")
    return redirect("/forgotpassword")
  except jwt.InvalidSignatureError:
    flash('envalid url')
    return redirect("/forgotpassword")
    #print(request.form.get("pass"))
  return render_template("home/newpassword.html")