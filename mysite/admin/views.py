from flask import render_template,request,redirect,url_for,flash
from flask_login import login_required,logout_user,login_user,current_user
from mysite.home.models import User
from .admin_permission import admin_allow
from mysite.blog.models import Blog

@admin_allow
def adminlogin():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]
    print(email,password)
    u = User.query.filter_by(email=email).first()
    if u:
      if u.email == email and u.password == password and u.is_admin == True:
        print("login admin")
        login_user(u,remember=True)
        return redirect(url_for('admin.home'))
      else:
        flash("envalid email or password")
        return redirect(url_for('admin.adminlogin'))
    else:
      flash("envalid email or password")
      return redirect(url_for('admin.adminlogin'))
  return render_template("admin/adminlogin.html")


def admin_logout():
  logout_user()
  return redirect(url_for('admin.adminlogin'))

@admin_allow
@login_required
def home():
  
  return render_template("admin/adminhome.html")


@admin_allow
@login_required
def adminrow(post):
  print(post)
  return render_template("admin/adminrow.html")