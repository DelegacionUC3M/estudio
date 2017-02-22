from .connection import db


class StudyGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    study = db.Column(db.String(150), nullable=False)
    school = db.Column(db.String(30), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    users = db.Table('users_belong_to_studygroups',
        db.Column('user_id', db.Integer,db.ForeignKey('users.id'), nullable=False,
        db.Column('studygroup_id',db.Integer,db.ForeignKey('studygroups.id'),nullable=False),
        db.PrimaryKeyConstraint('user_id', 'studygroup_id')))
    date = db.Column(db.DateTime)
    description = db.Column(db.String(255))
    place = db.Column(db.String(50))
    admins = db.Table('admins_of_studygroups',
        db.Column('user_id', db.Integer,db.ForeignKey('users.id'), nullable=False,
        db.Column('studygroup_id',db.Integer,db.ForeignKey('studygroups.id'),nullable=False),
        db.PrimaryKeyConstraint('user_id', 'studygroup_id')))


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
