from flask import Blueprint


frontend_views = Blueprint('frontend', __name__, url_prefix='/')


@frontend_views.route('/')
def index():
    return 'Hello Horus!'
