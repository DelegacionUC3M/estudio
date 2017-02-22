from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


users_groups = db.Table('users_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('groups_id', db.Integer, db.ForeignKey('study_group.id')))

admins_groups = db.Table('admins_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('groups_id', db.Integer, db.ForeignKey('study_group.id')))

class User(db.Model):	
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    name = db.Column(db.String(255), nullable=False)
    surname = db.Column(db.String(255), nullable=False)
    nia = db.Column(db.Integer, nullable=False)
    study = db.Column(db.Integer, nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    uid = db.Column(db.Integer)
    groups = db.relationship('StudyGroup', secondary=users_groups, backref=db.backref('users', lazy='dynamic'))
    admins = db.relationship('StudyGroup', secondary=admins_groups, backref=db.backref('admins', lazy='dynamic'))


    def __init__(self, name=None, surname=None, nia=None, contact=None):
        self.name = name
        self.surname = surname
        self.nia = nia
        self.contact = contact


    def __repr__(self):
    	
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'nia': self.nia,
            'study': self.study,
            'contact': self.contact,
            'groups': self.groups,
            'uid': self.uid
        }