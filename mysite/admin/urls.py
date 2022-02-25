from flask import Blueprint
from mysite import app
from .views import *
admin = Blueprint('admin',__name__)

admin.add_url_rule('/',view_func=home,methods=['GET','POST'])
admin.add_url_rule('/login/',view_func=adminlogin,methods=['GET','POST'])
admin.add_url_rule('/logout/',view_func=admin_logout,methods=['GET'])
admin.add_url_rule('/showrow/<post>/',view_func=adminrow,methods=['GET','POST'])