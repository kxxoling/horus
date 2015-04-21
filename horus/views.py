from flask import Blueprint
from flask import render_template


frontend_views = Blueprint('frontend', __name__, url_prefix='/')


@frontend_views.route('/')
def index():
    return render_template('index.jade', page_title='Welcome to Horus')


@frontend_views.route('resume/<int:resume_id>')
def resume(resume_id=None):
    if resume_id:
        print resume_id
    return render_template('resume.jade', content="""# Resume

sample resume

## Content

This is content!""")
