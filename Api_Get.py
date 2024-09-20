from flask import Flask, jsonify

# Crear una instancia de Flask
app = Flask(__name__)

# Definir una ruta para el método GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({"mensaje": "¡Hola, bienvenido a la API!"})


# Ejecutar la aplicación
if __name__ == '__main__':
    app.run(debug=True)
