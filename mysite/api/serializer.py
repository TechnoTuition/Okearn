from mysite import ma
from mysite.blog.models import Blog
class BlogSchema(ma.Schema):
  class Meta:
    fields = ("id","title","slug","body","post_created","post_image","use_id")
blog_schema = BlogSchema()
blogs_schema = BlogSchema(many=True)