from . import main
from flask import render_template

@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to Pitch Black'
    return render_template('index.html' , title = title)