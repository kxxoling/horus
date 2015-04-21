from flask import Flask
from flask import send_file
from flask.ext.admin import Admin
from jinja2 import Environment

from .admin import AdminRequiredView
from .models import User, Work, Company
from .views import frontend_views
from .models import db as main_db


def create_app(config=None):
    app = Flask(
        __name__,
        template_folder='templates'
    )

    if isinstance(config, dict):
        app.config.update(config)
    elif config:
        app.config.from_pyfile(config)

    #: prepare for database
    main_db.init_app(app)
    main_db.app = app
    main_db.create_all()

    register_jinja(app)
    register_static(app)
    register_routes(app)
    register_admin(app, main_db)

    return app


def register_routes(app):
    app.register_blueprint(frontend_views)
    return app


def register_admin(app, db):
    admin = Admin(app, endpoint='admin')
    admin.add_view(AdminRequiredView(User, db.session))
    admin.add_view(AdminRequiredView(Work, db.session))
    admin.add_view(AdminRequiredView(Company, db.session))


def register_static(app):
    @app.route('/<file_name>.txt')
    def plain_file(file_name):
        return send_file(file_name)
    return app


def register_jinja(app):
    app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')
    return app
