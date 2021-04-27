from flask import Flask, jsonify, render_template, redirect, request, flash #aquí importamos la librerías
from patentes import patentes # importamos el Modulo Patentes
from jinja2 import Environment, PackageLoader, select_autoescape # Importamos jinja2


#Inicialización
app = Flask('Proyecto Flask')
app = Flask(__name__,template_folder='templates')


#Tarea 1 endpoint 

# Routes to Render Something
@app.route('/', endpoint="home")
def Get():
    return render_template('index.html')


@app.route('/patentes/<string:id_patente>', methods=['GET','POST'])
def getPatente(id_patente):
    productFound = [patentes for patente in patentes if patentes['id_patente'] == numero_patente]
    return jsonify({"patente": productFound[0]})    


@app.route('/patentes', methods=['GET'])
def AgregarPatente():
    print(request.json)
    consulta = {
        "id_patente": request.json['id_patente'],
        "numero_patente": request.json['numero_patente']
    }
    patentes.append(consulta)
    return jsonify({"message": "Producto ok", "patentes": patentes})


# Get Patentes in Json
@app.route('/patentes', methods=['GET'])
def getPatentes():
    return jsonify({'patentes': patentes, "Mensaje": "Lista de Pantentes"})


#Tarea 2 endpoint Matrices 

# Endpoint Tarea 2
@app.route('/tarea2')
def tarea2():
    return jsonify({"Total Matriz": "Return"})


# Routes to Render Something
@app.route('/tarea2/respuesta', methods=['POST'])
def rtarea2():
    return 'test'


if __name__ == '__main__':
    app.run(debug=False)