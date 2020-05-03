from flask import render_template
from . import auth
from .. import db
from ..models import User

@auth.route('/login')
def login():
    return render_template('auth/login.html')