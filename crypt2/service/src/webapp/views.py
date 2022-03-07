from flask import render_template, request, Response, abort, send_file, make_response
from webapp.util import encrypt,decrypt
from webapp import app

FLAG = "[REDACTED]"

def check_session():
  try:
    cookie_val = request.cookies.get('username',"")
    username = decrypt(cookie_val)
  except Exception as e:
    print(e)
    username = ""
  if not isinstance(username,str):
      username = username.decode("utf-8")
  return username

@app.route('/')
@app.route('/index')
def index():
  username= check_session()
  if username != "":
    return render_template('successful_login.html', username=username)
  else:
    return render_template('index.html')

@app.route('/logout', methods = ['GET'])
def logout():
  resp = make_response(render_template('logout.html'))
  resp.set_cookie('username', '', expires=0)
  return resp

@app.route('/login', methods = ['POST'])
def login():
  username = request.form.get("name")
  password = request.form.get("pass")
  if isinstance(username,str):
      username = username.encode("utf-8")
  if b"admin" in username:
    return render_template('bad_login.html')
  else: 
    cookie = encrypt(username)
    resp = make_response(render_template('successful_login.html', username = username.decode("utf-8")))
    resp.set_cookie('username',cookie)
    return resp

@app.route('/admin', methods = ['GET'])
def show_admin():
  try:
    username = check_session()
  except Exception as e:
    print(e)
    return ""
  if username == "admin":
      return render_template('admin.html', flag=FLAG)
  else:
    return ""
