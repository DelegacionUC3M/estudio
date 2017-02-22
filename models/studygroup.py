from .connection import db


admins_groups = db.Table('admins_groups',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('groups_id', db.Integer, db.ForeignKey('study_group.id')))


class StudyGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    study = db.Column(db.String(150), nullable=False)
    school = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    place = db.Column(db.String(50), nullable=False)
    admins = db.relationship('User', secondary=admins_groups, backref=db.backref('admin_groups', lazy='dynamic'))


    def __init__(self, study=None, school=None, subject=None, users=None, date=None, description=None, place=None, admins=None):
        self.study = study
        self.school = school
        self.subject = subject
        self.users = users
        self.date = date
        self.description = description
        self.place = place
        self.admins = admins


    def __repr__(self):
        return {
            'id' : self.id,
            'school' = self.school,
            'subject' = self.subject,
            'users' = self.users,
            'date' = self.date,
            'description' = self.description,
            'place' = self.place,
            'admins' = self.admins
        }
