from mysite import app
from flask import Blueprint
from .views import *
api = Blueprint('api',__name__)


api.add_url_rule('/',view_func=api_docs,methods=['GET'])
api.add_url_rule('/users/',view_func=all_user,methods=['GET'])
api.add_url_rule('/user/<id>/',view_func=single_user,methods=['GET','POST'])
api.add_url_rule('/post',view_func=all_post)
