from flask import Flask, render_template, url_for, flash, redirect
from flask_login import login_required, current_user
from your_application import db  
from your_application.models import Post
from your_application.forms import PostForm

app = Flask(__name__)  

from your_application import db
from your_application.models import Post


db.create_all()
