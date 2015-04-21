from flask import Blueprint
from flask import render_template


frontend_views = Blueprint('frontend', __name__, url_prefix='/')


@frontend_views.route('/')
def index():
    return render_template('index.jade', page_title='Welcome to Horus')
