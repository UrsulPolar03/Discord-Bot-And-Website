from flask import Flask, redirect, url_for, render_template, request, session
from threading import Thread
from history import *
from oauth import Oauth
import time

app = Flask('__name__')
app.config["SECRET_KEY"] = "test123"

if __name__ == "__main__":  
  app.run(debug=True)

time.sleep(20)


def listToString(s): 
    str1 = "" 
    for ele in s: 
        str1 += ele +"\n"  
    return str1 


@app.route('/')
def login():
  return render_template("login.html", discord_url=Oauth.discord_login_url)


@app.route('/acasa')
def home():
  code = request.args.get("code")
  at = Oauth.get_access_token(code)
  session["token"] = at
  user = Oauth.get_user_json(at)
  user_name = user.get("username")
  user_id = user.get("discriminator")
  print(user)
  print(code)
  print("Username:" + user_name)
  print("ID:" + user_id)
  return render_template("index.html", name = user.get("username"), idu =user.get("discriminator"), content = history)

def run():
  app.run(host='0.0.0.0', port=8000)

def keep_alive():
  t = Thread(target=run)
  t.start()


