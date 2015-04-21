from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin import Admin

from .models import User, Work, Company, Resume


class AdminRequiredView(ModelView):
    def is_accessible(self):
        return True


def register_admin(app, db):
    admin = Admin(app, endpoint='admin')
    admin.add_view(AdminRequiredView(User, db.session))
    admin.add_view(AdminRequiredView(Work, db.session))
    admin.add_view(AdminRequiredView(Company, db.session))
    admin.add_view(AdminRequiredView(Resume, db.session))