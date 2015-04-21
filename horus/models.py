from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class BasicModel(object):

    id_ = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def to_dict(self):
        raise NotImplementedError       # Exception('NotImplemented')

    def to_json(self):
        pass

    def __unicode__(self):
        return "<Model %s>%d: %s" % (self.__name__, self.id_, self.name)


class User(BasicModel, db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String(50))
    family_name = db.Column(db.String(100))
    register_time = db.Column(db.DateTime)
    role = db.Column(db.Integer)


class Company(BasicModel, db.Model):
    __tablename__ = 'companies'

    register_time = db.Column(db.DateTime)
    scale = db.Column(db.String(100))
    bonus = db.Column(db.String(500))


class Work(BasicModel, db.Model):
    __tablename__ = 'works'

    publish_time = db.Column(db.DateTime)
    description = db.Column(db.String(1000))
    is_effective = db.Column(db.Boolean)


class Resume(BasicModel, db.Model):
    __tablename__ = 'resumes'

    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)
    content = db.Column(db.Text)