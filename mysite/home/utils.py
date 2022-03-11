from mysite import app ,mail,final
from flask_mail import Message
#from .views import final
def email_verification(url,email):
  
  msg = Message("Please verify your email",sender="noreply@okearn.com",recipients=[email])
  msg.body = f"""To verify your email address
  Email Verification 
  This url available only 2 minute
  Verification Code: {url}
  """
  mail.send(msg)
def reset_pass_mail(URL, email):
  msg = Message("Password reset link",sender="noreply@okearn.com",recipients=[email]  )
  msg.body = f"""
  To reset your Password click this link and this is available only 2 minutes 
  click: {URL}
  """
  mail.send(msg)
  