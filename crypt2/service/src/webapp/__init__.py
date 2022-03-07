from flask import Flask, session
import os, sys, atexit
import secrets, string
from werkzeug.serving import is_running_from_reloader
def create_app():
  app = Flask(__name__)
  app.secret_key = ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(16))

  return app
app = create_app()

from webapp import views
