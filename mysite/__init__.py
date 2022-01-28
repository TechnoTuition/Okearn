from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_socketio import SocketIO
from flask_ckeditor import CKEditor
from flask_debugtoolbar import DebugToolbarExtension
from flask_marshmallow import Marshmallow
from os import environ
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
#--------------CKEditor--------------------

ckeditor = CKEditor(app)

#---------Bcrypt------------------
bcrypt = Bcrypt(app)
#--------------SocketIo--------------
socketio = SocketIO(app)

#----------LoginManager-------------
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "home.user_login"
login_manager.login_message_category = "success"

app.config['SECRET_KEY'] = environ['SECRET_KEY']

#-------- DebugToolbarExtension ----------
app.debug = True
#toolbar = DebugToolbarExtension(app)
#=======DATABASE==============
app.config['SQLALCHEMY_DATABASE_URI'] = environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = environ['SQLALCHEMY_TRACK_MODIFICATIONS']
db = SQLAlchemy(app)

#-------------MarshMallow---------------
ma = Marshmallow(app)

#------------Flask-Mail--------------
app.config['MAIL_SERVER'] = environ['MAIL_SERVER']
app.config['MAIL_PORT']  = environ['MAIL_PORT']
app.config['MAIL_USERNAME'] = environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = environ['MAIL_PASSWORD']
#app.config['MAIL_USE_TLS'] = environ['MAIL_USE_TLS']
app.config['MAIL_USE_SSL'] = environ['MAIL_USE_SSL']

mail = Mail(app)
#------------Random Number Genrate--------------
import random
import string

num = list(string.digits)
shuffleNum = random.shuffle(num)
totalnum = "".join(num)
final = totalnum[:6]

#----------App Register----------

from mysite.blog.views import blog
from mysite.user.views import user
from mysite.home.views import home
from mysite.api.views import api

app.register_blueprint(blog,url_prefix='/blog')
app.register_blueprint(user,url_prefix='/user')
app.register_blueprint(home,url_prefix='/')
app.register_blueprint(api,url_prefix='/api')
