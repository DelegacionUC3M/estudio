from flask import Flask
from flask import request
from models.connection import db
from models import StudyGroup

# Inicializacion del objeto Flask
app = Flask(__name__)

# Generacion del dict (diccionario) de configuracion desde fichero
app.config.from_pyfile('config.cfg')

# Enlaza la aplicacion y la base de datos
db.app = app
db.init_app(app)

# Url /
@app.route('/')
def index():
    return 'Hola mundo'


@app.route('/studygroups', methods = ['POST'])
def createStudyGroup():
    data = request.json
    studygroup = StudyGroup(int(data['study']), int(data['school']), data['subject'])

    #Optional values
    if 'date' in data.keys():
        studygroup.data = data['date']

    if 'description' in data.keys():
        studygroup.description = data['description']

    if 'place' in data.keys():
        studygroup.place = data['place']

    db.session.add(studygroup)
    db.session.commit()

    return studygroup.__repr__()


@app.route('/studygroups', methods = ['GET'])
def showStudyGroup():
    #TODO
    pass

if __name__ == '__main__':
    app.run()
