from flask import Blueprint
from flask import render_template
from .models import Resume


frontend_views = Blueprint('frontend', __name__, url_prefix='/')


@frontend_views.route('/')
def index():
    return render_template('index.jade', page_title='Welcome to Horus')


@frontend_views.route('resume/')
def list_resumes():
    resume_list = Resume.query.all()
    return render_template('resume_list.jade', resume_list=resume_list)


@frontend_views.route('resume/<int:resume_id>/')
def show_resume(resume_id=None):
    resume = Resume.query.get_or_404(resume_id)

    return render_template('resume.jade', resume=resume)