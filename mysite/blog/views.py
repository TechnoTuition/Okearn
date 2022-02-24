from flask import Blueprint,render_template,request,flash,redirect,url_for,jsonify
from flask_login import login_required,current_user
from mysite import db
from .models import Blog,Like
from mysite.home.models import User,Fallow
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

# read detail post
@blog.route('/read/<string:slug>/',methods=["GET","POST"])
@login_required
def read_post(slug):
  posts = Blog.query.filter_by(slug=slug).first()
  posts.views = posts.views + 1
  db.session.add(posts)
  db.session.commit()
  data = current_user.id in map(lambda x: x.user_id,posts.like)
  
  return render_template("blog/readpost.html",posts=posts,user=current_user.id,like=data)

#edit posts
@blog.route('/edit/<int:id>/')
def edit_post(id):
  print(id)
  post = Blog.query.filter_by(id=id).first()
  print(post)
  data = {}
  data['id'] = post.id
  data['title'] = post.title
  data['slug'] = post.slug
  data['like'] = len(post.like)
  
  #data['body'] = post.body
  data['post_created'] = post.post_created
  return jsonify({'post': data})


# like handel 
@blog.route('/like/<string:post_id>/',methods=['POST','GET'])
@login_required
def post_like(post_id):
  posts = Blog.query.filter_by(id=post_id).first()
  print(request.url)
  like = Like.query.filter_by(user_id=current_user.id,post_id=post_id).first()
  if like:
    db.session.delete(like)
    db.session.commit()
    
  else:
    like = Like(user_id=current_user.id,post_id = post_id)
    db.session.add(like)
    db.session.commit()
  
  return jsonify({'like': len(posts.like),'liked': current_user.id in map(lambda x: x.user_id,posts.like)})

# follow user
@blog.route('/fallow/<user_id>/',methods=['GET','POST'])
@login_required
def fallow_user(user_id):
  print(request.url)
  user = User.query.filter_by(id=user_id).first()
  print(len(user.fallowing))
  data = []
  for fallow in user.fallowing:
    data.append(fallow.id)
  if current_user.id in data:
    fallower = Fallow.query.filter_by(id=current_user.id).first()#
    user.fallowing.remove(fallower)
    db.session.commit()
    
  else:
  # get post related user id
   fallower = Fallow.query.filter_by(id=current_user.id).first()#
   user.fallowing.append(fallower)
   db.session.add(user)
   db.session.commit()
  return jsonify({'fallower': len(user.fallowing),'fallowed': True})
