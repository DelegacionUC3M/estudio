from .connection import db


class StudyGroup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    study = db.Column(db.Integer, nullable=False)
    school = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(500), nullable=False)
    date = db.Column(db.DateTime)
    description = db.Column(db.Text)
    place = db.Column(db.String(500))

    def __init__(self, name=None, study=None, school=None, subject=None):
        self.name = name
        self.study = study
        self.school = school
        self.subject = subject

    def __repr__(self):
        return str({
            'id': self.id,
            'name': self.name,
            'school': self.school,
            'subject': self.subject,
            'users': self.users,
            'date': self.date,
            'description': self.description,
            'place': self.place,
            'admins': self.admins
        })
