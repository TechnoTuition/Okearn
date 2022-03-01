from argparse import ArgumentParser
from mysite import db,app,bcrypt
from mysite.home.models import User,Fallow
import getpass
from colorama import init,Fore,Style
import os
import sys


parser = ArgumentParser(usage='web app <command> ')
parser.add_argument("-r","--run",action='store_true',help="Run for development server")
parser.add_argument("-a","--admin",action='store_true',help="Create admin user")
args = parser.parse_args()

init()
def createAdminUser():
  try:
    email = input(f"Email:{Style.BRIGHT}{Fore.GREEN}")
    Style.RESET_ALL
    dbqueryEmail = User.query.filter_by(email=email).first()
    if dbqueryEmail:
      print(f"{Style.BRIGHT}{Fore.RED}that  email already exist{Style.RESET_ALL}")
    else:
      print(Style.RESET_ALL)
      password = getpass.getpass()
      conformPass = getpass.getpass("ConformPassword: ")
      if password == "" and conformPass == "":
        print(f"{Style.BRIGHT}{Fore.RED}password are not blank{Style.RESET_ALL}")
      elif password != conformPass:
        print(f"{Style.BRIGHT}{Fore.RED}Password and ConformPassword not are same{Style.RESET_ALL}")
      else:
        hashpass = bcrypt.generate_password_hash(password).decode("utf-8")
        u = User(firstname="admin",lastname="u",email=email,is_admin=True,password=hashpass)
        new_fallow = Fallow()
        db.session.add(new_fallow)
        db.session.add(u)
        db.session.commit()
        print(f"{Style.BRIGHT}{Fore.CYAN}admin acconut created...{Style.RESET_ALL}")
  except KeyboardInterrupt:
    sys.exit()
def runDevelopmentServer():
  try:
    app.run(host="0.0.0.0",debug=True,port=os.environ['PORT'])
  except KeyboardInterrupt:
    sys.exit()

if args.admin:
  createAdminUser()
elif args.run:
  runDevelopmentServer()