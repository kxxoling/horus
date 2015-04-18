from flask.ext.admin.contrib.sqla import ModelView


class AdminRequiredView(ModelView):
    def is_accessible(self):
        return True
