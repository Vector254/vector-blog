from flask import Flask, render_template
from . import main
from ..models import Posts
from .forms import CommentForm,PostForm
from flask_login import login_required, current_user

@main.route('/')
def index():

    posts = Posts.query.order_by(Posts.date_posted.desc()).all()
    return render_template('index.html',posts = posts)

@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/post', methods = ['GET','POST'])
@login_required
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
    return render_template('posts.html',form=form)



@main.route('/comment/<int:post_id>', methods = ['GET','POST'])
@login_required
def new_comment():
    form = CommentForm()
    post=Posts.query.get(post_id)
    if form.validate_on_submit():
        post = form.post.data

        new_comment = Comment(post=post,user_id = current_user._get_current_object().id, post_id = post_id)
        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for('.new_comment', post_id= post_id))
    all_comments = Comment.query.filter_by(post_id = post_id).all()
    return render_template('comments.html', form = form,comment = all_comments )

