from flask import Blueprint
from flask import render_template
from flask import url_for, session, request, jsonify, redirect
from flask.ext.oauthlib.client import OAuth

from .models import Resume


frontend_views = Blueprint('frontend', __name__, url_prefix='/')

oauth_views = Blueprint('oauth', __name__, url_prefix='/oauth/')

oauth = OAuth()
github = oauth.remote_app(
    'github',
    consumer_key='08db72ce47a207704fb4',
    consumer_secret='f5e5eff75760ea886e033a6ec87b23d33d4903a0',
    request_token_params={'scope': 'user:email'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)


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


@oauth_views.route('login/')
def login():
    return github.authorize(callback=url_for('oauth.authorized', _external=True))


@oauth_views.route('logout')
def logout():
    session.pop('github_token', None)
    return redirect(url_for('frontend.index'))


@oauth_views.route('login/authorized')
def authorized():
    resp = github.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error'],
            request.args['error_description'],
        )
    session['github_token'] = (resp['access_token'], '')
    user = github.get('user')
    flash('%s, Welcome!' % user.data['name'])
    return redirect('/')


@github.tokengetter
def get_github_oauth_token():
    return session.get('github_token')
