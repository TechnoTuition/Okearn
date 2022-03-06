import secrets
import os 
from mysite import app
from PIL import Image
def save_image(img):
  
  fname,fext = os.path.splitext(img.filename)
  print(fname, fext)
  random_hex = secrets.token_hex(16)
  print(random_hex)
  pic_name = random_hex+fext
  print(pic_name)
  path = os.path.join(app.root_path,'static/media/profile_pic',pic_name)
  
  i = Image.open(img)
  size = (124,124)
  i.thumbnail(size)
  i.save(path)
  return pic_name