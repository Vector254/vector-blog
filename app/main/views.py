from flask import Flask, render_template
from . import main

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/post')
def post():
    return render_template('post.html')

@main.route('/comment')
def comment():
    return render_template('comment.html')