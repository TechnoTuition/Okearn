from flask import Blueprint,render_template,request,flash,redirect,url_for,session,jsonify
from .forms import RegisterForm,LoginForm,EmailVerificationForm
from .models import User
from mysite.blog.models import Blog
from mysite import bcrypt,db,mail,final,socketio
from flask_login import login_user,current_user,login_required,logout_user
from .utils import email_verification
import json 
from flask_socketio import send

home = Blueprint('home',__name__)

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)
    send(data)
@home.route('/')
def index():
  post = Blog.query.all()
  print(post)
  return render_template("home/index.html",posts=post)
# register form 
@home.route('/register/',methods=['GET','POST'])
def user_register():
  if current_user.is_authenticated:
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
        
        # get all data
        
        session['firstname'] = form.firstname.data
        session['lastname'] = form.lastname.data
        session['email'] = form.email.data
        session['password'] = form.password.data
        session['final'] = final
        email_verification(form.email.data)

        return redirect(url_for("home.email_verify"))
  else:
    form = RegisterForm()
  return render_template('home/signup.html',form=form)


# login form 
@home.route('/login/',methods=["GET","POST"])
def user_login():
  if current_user.is_authenticated:
    return redirect(url_for("user.index"))
  if request.method == "POST":
    form = LoginForm()
    if form.validate_on_submit():
      user = User.query.filter_by(email=form.email.data).first()
      if user and bcrypt.check_password_hash(user.password,form.password.data):
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
@home.route('/email_verification/',methods=["GET","POST"])
def email_verify():
  if request.method == "POST":
    firstname = session["firstname"]
    lastname = session["lastname"]
    email = session["email"]
    password = session["password"]
    final = session["final"]
    
    form = EmailVerificationForm()
    
    if form.validate_on_submit():
      
      if final == str(form.code.data):
        print(final,form.code.data)
        pass_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(firstname=firstname,lastname= lastname,email=email,password=pass_hash)
        db.session.add(new_user)
        db.session.commit()
        for key in list(session.keys()):
          session.pop(key)
        flash("Account hase been created ")
        return redirect(url_for("home.user_login"))
      else:
        flash("wrong code")
  else:
    if 'email' in session:
      flash("verify email")
    else:
      return redirect("/")
    form = EmailVerificationForm()
  return render_template("home/email_verification.html",form=form)
# chat route

@home.route('/chat/',methods=["GET","POST"])
def chat_user():
  return render_template('home/chat.html')