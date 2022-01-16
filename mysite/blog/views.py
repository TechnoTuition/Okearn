from flask import Blueprint,render_template,request,flash,redirect,url_for
from flask_login import login_required,current_user
from mysite import db
from .models import Blog
from .forms import PostForm

blog = Blueprint('blog',__name__)


@blog.route('/',methods=["GET","POST"])
@login_required
def index():
  print("Hello",current_user.id)
  if request.method == "POST":
    
    form = PostForm()
    if form.validate_on_submit():
      title = form.title.data
      body = form.body.data
      # title convert into slug
      data = title.split()
      tuple(data)
      slug = "-".join(data)
      print(title)
      print(slug)
      blog = Blog(title=form.title.data,slug=slug,body=form.body.data,user_id=current_user.id)
      db.session.add(blog)
      db.session.commit()
      flash("write post")
      print(title,body)
  else:
    form = PostForm()
  return render_template('blog/index.html',form=form)

@blog.route('/read/<title>/',methods=["GET","POST"])
@login_required
def read_post(title):
  return render_template("blog/readpost.html")