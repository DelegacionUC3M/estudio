import time

from .connection import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    study_group = db.Column(db.Integer, db.ForeignKey('study_group.id'), nullable=False)
    sender = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    send = db.Column(db.DateTime, nullable=False)

    def __init__(self, study_group, sender, content):
        self.study_group = study_group
        self.sender = sender
        self.content = content
        self.send = time.time()

    def __repr__(self):
        return str({
            'id': self.id,
            'study_group': self.study_group,
            'sender': self.sender,
            'content': self.content,
            'send': self.send
        })
