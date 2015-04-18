from flask.ext.admin import Admin
from .admin import AdminRequiredView
from .models import User, Work, Company
from .views import frontend_views
from .apps import app
from .models import db


admin = Admin(app, endpoint='admin')

admin.add_view(AdminRequiredView(User, db.session))
admin.add_view(AdminRequiredView(Work, db.session))
admin.add_view(AdminRequiredView(Company, db.session))

app.register_blueprint(frontend_views)

db.create_all()
