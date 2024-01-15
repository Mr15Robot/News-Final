from flask import render_template
from datetime import datetime


from models import Post

@app.route('/latest')
def latest():

    january_posts = Post.query.filter(db.func.strftime("%m", Post.date) == '01').all()

    return render_template('latest.html', posts=january_posts)
