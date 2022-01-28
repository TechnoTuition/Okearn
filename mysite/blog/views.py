from flask import Blueprint,render_template,request,flash,redirect,url_for,jsonify
from flask_login import login_required,current_user
from mysite import db
from .models import Blog,Like
from .forms import PostForm

blog = Blueprint('blog',__name__)

@blog.route('/',methods=["GET","POST"])
@login_required
def index():
  if request.method == "POST":
    
    form = PostForm()
    if form.validate_on_submit():
      title = form.title.data
      body = form.body.data
      # title convert into slug
      data = title.split()
      tuple(data)
      slug = "-".join(data)
      blog = Blog(title=form.title.data,slug=slug,body=form.body.data,user_id=current_user.id)
      db.session.add(blog)
      db.session.commit()
      flash("write post")
  else:
    form = PostForm()
  return render_template('blog/index.html',form=form)

@blog.route('/read/<string:slug>/',methods=["GET","POST"])
@login_required
def read_post(slug):
  posts = Blog.query.filter_by(slug=slug).first()
  return render_template("blog/readpost.html",posts=posts)
  
@blog.route('/like/<string:post_id>/',methods=['POST'])
@login_required
def post_like(post_id):
  posts = Blog.query.filter_by(id=post_id).first()
  print("post data",posts)
  like = Like.query.filter_by(user_id=current_user.id,post_id=post_id).first()
  if like:
    db.session.delete(like)
    db.session.commit()
  
  else:
    like = Like(user_id=current_user.id,post_id = post_id)
    db.session.add(like)
    db.session.commit()
  
  return jsonify({'like': len(posts.like)})