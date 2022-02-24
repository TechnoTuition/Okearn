from flask_login import current_user
from flask import redirect,render_template,url_for
from functools import wraps
def admin_allow(f):
  @wraps(f)
  def decorator(*args,**kwargs):
    if current_user.is_authenticated:
      if current_user.is_admin == True:
        return render_template("admin/adminhome.html")
      elif current_user.is_admin == False:
        return render_template("admin/adminlogin.html")
    return f(*args,**kwargs)
  return decorator
  