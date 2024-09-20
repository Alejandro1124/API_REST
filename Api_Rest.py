from flask import Flask, jsonify, request

# Crear una instancia de Flask
app = Flask(__name__)


# Ruta que maneja los métodos GET, POST, PUT, y DELETE
@app.route('/saludo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo():
    if request.method == 'GET':
        return jsonify({"mensaje": "¡Has llamado al método GET en la ruta /saludo!"})

    elif request.method == 'POST':
        return jsonify({"mensaje": "¡Has llamado al método POST en la ruta /saludo!"})

    elif request.method == 'PUT':
        return jsonify({"mensaje": "¡Has llamado al método PUT en la ruta /saludo!"})

    elif request.method == 'DELETE':
        return jsonify({"mensaje": "¡Has llamado al método DELETE en la ruta /saludo!"})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
