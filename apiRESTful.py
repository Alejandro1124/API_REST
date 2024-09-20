# Importamos las librerías necesarias
from flask import Flask, request, jsonify  # Flask para crear la aplicación web y request/jsonify para manejar solicitudes/respuestas
import requests  # Requests nos permite hacer solicitudes HTTP a APIs externas

# Crear la instancia de la aplicación Flask
app = Flask(__name__)  # __name__ le dice a Flask el nombre del módulo actual, útil para encontrar recursos y definir rutas

# Definir la URL base de la API externa (en este caso, un Mock API que simula un servicio de coches)
BASE_URL = 'https://66eb03e355ad32cda47b5d10.mockapi.io/IoTCarStatus'

# Definir una ruta para obtener todos los coches
@app.route('/cars', methods=['GET'])  # Este decorador indica que cuando accedas a /cars con el método GET, se ejecuta la función
def get_all_cars():
    response = requests.get(BASE_URL)  # Hacemos una solicitud GET a la API externa para obtener todos los coches
    return jsonify(response.json()), response.status_code  # Convertimos la respuesta a JSON y devolvemos el código de estado (200, 404, etc.)

# Definir una ruta para obtener un coche específico por ID
@app.route('/cars/<int:id>', methods=['GET'])  # <int:id> es un parámetro dinámico, donde se espera un ID de tipo entero
def get_car_by_id(id):
    response = requests.get(f'{BASE_URL}/{id}')  # Hacemos una solicitud GET a la API para obtener un coche con el ID proporcionado
    return jsonify(response.json()), response.status_code  # Devolvemos los datos del coche en formato JSON junto con el código de estado

# Definir una ruta para crear un nuevo coche
@app.route('/cars', methods=['POST'])  # POST se utiliza cuando queremos crear un nuevo recurso en el servidor
def create_car():
    data = request.json  # request.json captura los datos enviados en la solicitud en formato JSON
    response = requests.post(BASE_URL, json=data)  # Enviamos los datos como un JSON al API externo usando POST
    return jsonify(response.json()), response.status_code  # Devolvemos la respuesta del API que contiene el coche recién creado y su código de estado

# Definir una ruta para actualizar un coche existente
@app.route('/cars/<int:id>', methods=['PUT'])  # PUT se usa cuando queremos actualizar un recurso existente
def update_car(id):
    data = request.json  # request.json captura los datos actualizados en la solicitud
    response = requests.put(f'{BASE_URL}/{id}', json=data)  # Enviamos una solicitud PUT con los datos actualizados para el coche con el ID especificado
    return jsonify(response.json()), response.status_code  # Devolvemos la respuesta con el coche actualizado y el código de estado

# Definir una ruta para eliminar un coche
@app.route('/cars/<int:id>', methods=['DELETE'])  # DELETE se usa para borrar un recurso específico, en este caso un coche
def delete_car(id):
    response = requests.delete(f'{BASE_URL}/{id}')  # Enviamos una solicitud DELETE al API para eliminar el coche con el ID dado
    return jsonify({"message": "Car deleted successfully"}), response.status_code  # Devolvemos un mensaje de éxito y el código de estado de la operación

# Iniciar la aplicación Flask
if __name__ == '__main__':  # Esta condición asegura que el servidor Flask solo se ejecutará si este archivo es el principal
    app.run(debug=True)  # Ejecuta la aplicación en modo depuración, lo que es útil para ver errores detallados durante el desarrollo
