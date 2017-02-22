from .connection import db


users_groups = db.Table('users_groups',
                        db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                        db.Column('groups_id', db.Integer, db.ForeignKey('study_group.id')))

admins_groups = db.Table('admins_groups',
                         db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
                         db.Column('groups_id', db.Integer, db.ForeignKey('study_group.id')))


class User(db.Model):	
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    nia = db.Column(db.Integer, nullable=False)
    study = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer)
    groups = db.relationship('StudyGroup', secondary=users_groups, backref=db.backref('users', lazy='select'))
    admin_groups = db.relationship('StudyGroup', secondary=admins_groups, backref=db.backref('admins', lazy='select'))

    def __init__(self, name=None, surname=None, nia=None, study=None, contact=None):
        self.name = name
        self.surname = surname
        self.nia = nia
        self.study = study
        self.contact = contact

    def __repr__(self):
        return str({
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'nia': self.nia,
            'study': self.study,
            'contact': self.contact,
            'groups': self.groups,
            'uid': self.uid,
            'admin_groups': self.admin_groups
        })
