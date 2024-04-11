#*************************************
from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
#Estructura basica del ejemplo 2.1 y 2.2


#*******************************************
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
#Parte del Codigo del Ejemplo 2.2

#**************************
if __name__ == '__main__':
    app.run(debug=True)
#Codigo añadido para el funcionamiento del ejemplo 2.1 y 2.2   