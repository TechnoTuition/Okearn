from mysite import app ,mail,final
from flask_mail import Message
#from .views import final
def email_verification(email):
  
  msg = Message("Please verify your email",sender="noreply@okearn.com",recipients=[email])
  msg.body = f"""To verify your email address
  Email Verification 
  Verification Code: {final}
  {type(final)}"""
  mail.send(msg)