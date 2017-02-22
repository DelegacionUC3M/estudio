from .connection import db


class Notify(db.Model):
    # Id siempre aparecera, aunque no lo hayamos contemplado en la tabla
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    topic = db.Column(db.String(255), nullable=False)
    # Clave foranea: nombre_tabla.nombre_atributo
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content = db.Column(db.Text, nullable=False)
    message_read = db.Column(db.Boolean, nullable=False)
    sent_date = db.Column(db.DateTime)
    label = db.Column(db.String(255))

    def __init__(self, topic=None, content=None, user=None, message_read=False):
        '''Funcion de construccion del objeto. Los que no pueden ser nullable los
         ponemos a False para poder crear un objeto vacío con sus atributos.'''
        # Igualamos a None para poder crear un NMessage vacio
        self.topic = topic
        self.content = content
        self.user = user
        self.message_read = message_read


    def __repr__(self):
        '''Llamamos a esta funcion para imprimir datos de forma semantica.'''
        # Los diccionarios en Python llevan por debajo un método __repr__ que se encarga de imprimirlos bonitos :) 
        # Además, nos viene bien para poder pasar el contenido de nuestra Clase en formato de Objeto JSON
        return {
            'id': self.id,
            'topic': self.topic,
            'user': self.user,
            'content': self.content,
            'message_read': self.message_read,
            'sent_date': self.sent_date,
            'label': self.label
        }
