from flask import render_template,request,redirect,url_for,flash
from flask_login import login_required,logout_user,login_user,current_user
from mysite.home.models import User
from mysite.blog.models import Blog
from mysite import bcrypt,db

def adminlogin():
  if request.method == "POST":
    email = request.form["email"]
    password = request.form["password"]
    print(email,password)
    u = User.query.filter_by(email=email).first()
    if u:
      hashpass = bcrypt.check_password_hash(u.password,password)
      print(hashpass)
      if u.email == email and hashpass == True and u.is_admin == True:
        print("login admin")
        login_user(u,remember=True)
        print("admin success")
        return redirect(url_for("admin.home"))
      else:
        flash("envalid email or password")
        return redirect(url_for('admin.adminlogin'))
    else:
      flash("envalid email or password")
      return redirect(url_for('admin.adminlogin'))
  return render_template("admin/adminlogin.html")

@login_required
def admin_logout():
  logout_user()
  return redirect(url_for('admin.adminlogin'))


@login_required
def home():
  if current_user.is_admin == True:
    table_names = []
    for t in db.engine.table_names():
      capable = t.capitalize()
      table_names.append(capable)
    return render_template("admin/adminhome.html",table = table_names)
  elif current_user.is_admin == False:
    print("hhh")
    return render_template("admin/adminlogin.html")
  return render_template("admin/adminhome.html")


@login_required
def adminrow(table):
  if current_user.is_admin == True:
    from sqlalchemy import text
    # select table related data
    sql = text(f'select * from {table}')
    result = db.engine.execute(sql)
    
    d = []
    for i in result:
      d.append(i)
    
    # select table columns
    u = []
    t = table
    #print(type(t))
    print(type(User))
    sqll = text(f"PRAGMA table_info({table});")
    user = db.engine.execute(sqll)
    for i in user:
      a = i[1]
      u.append(a)
    
    return render_template("admin/adminrow.html",d=d,u=u)
  elif current_user.is_admin == False:
    return render_template("admin/adminlogin.html")
  return render_template("admin/adminrow.html")