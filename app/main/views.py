from . import main
from flask import render_template
from ..models import Pitch, Comment, User, Upvote, Downvote
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Pitch Black'
    return render_template('index.html' , title = title)