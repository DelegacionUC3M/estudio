from .connection import db


class Notify(db.Model):
    # Id siempre aparecera, aunque no lo hayamos contemplado en la tabla
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    topic = db.Column(db.String(255), nullable=False)
    # Clave foranea: nombre_tabla.nombre_atributo
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    content = db.Column(db.Text, nullable=False)
    message_read = db.Column(db.Boolean, nullable=False)
    sent_date = db.Column(db.DateTime)
    label = db.Column(db.String(255))


    def __init__(self, topic=None, content=None, user=None, message_read=False,):
        # Igualamos a None para poder crear un NMessage vacio
        self.topic = topic
        self.content = content
        self.user = user
        self.message_read = message_read


    def __repr__(self):
        '''Llamamos a esta funcion para imprimir datos'''
        return {
            'id': self.id,
            'topic': self.topic,
            'user': self.user,
            'content': self.content,
            'message_read': self.message_read,
            'sent_date': self.sent_date,
            'label': self.label
        }