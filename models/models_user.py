from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''Clara, Axel, los comentarios son aquello de lo que no estoy seguro. Ej:
no sabía si poner self.group o self.group[], nullable = true o no escribir nada...
Gracias por su atención.'''


class User(db.Model):	
    id = db.Column(db.Integer, primary_key=True, autoincrement=1)
    name = db.Column(db.String(255), nullable = False)
    surname = db.Column(db.String(255), nullable = False)
    nia = db.Column(db.Integer, nullable = False)
    #study[] = db.Column()
    contact = db.Column(db.Integer, nullable = False)
    #groups[] = db.Column()
    uid = db.Column(db.Integer, '''nullable = True''')

    def __init__(self, name=None, surname=None, nia=None, study[]=None, contact=None, groups[]=None''', uid'''):
   
        self.name = name
        self.surname = surname
        self.nia = nia
        self.study[] = study[]
        self.contact = contact
        self.groups[] = groups
        #self.uid = uid


    def __repr__(self):
    	
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname,
            'nia': self.nia,
            'study[]': self.study[],
            'contact': self.contact,
            'groups[]': self.groups[],
            'uid': self.uid
        }