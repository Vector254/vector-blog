from flask import Flask, render_template
from . import main
from ..models import Posts
from .forms import CommentForm,PostForm

@main.route('/')
def index():

    posts = Posts.query.order_by(Posts.date_posted.desc()).all()
    return render_template('index.html',posts = posts)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required



@main.route('/post')
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = form.post.data
        owner_id = current_user
        title = form.title.data
        author = form.author.data
        new_post = Posts(owner_id =current_user._get_current_object().id,post=post,author=author,title=title)
        new_post.save_post()

        return redirect(url_for('main.index'))
    return render_template('post.html',form=form)

@main.route('/comment')
def comment():
    return render_template('comment.html')