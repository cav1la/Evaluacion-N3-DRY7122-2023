# Importar las librerías necesarias
import random  # Para generar números aleatorios
import csv  # Para trabajar con archivos CSV
from bottle import Bottle, request, static_file  # Para crear el servidor web

app = Bottle()

jugadores = []
jugadas = []
jugadas_csv = []

@app.get('/backend/api/juego/disponible')
def juego_disponible():
    estado_juego = 'disponible'  # Obtén el estado del juego desde donde sea que lo almacenes

    if estado_juego == 'disponible':
        return {'estado': 'disponible', 'id_juego': 123}  # Cambia el ID del juego según corresponda
    else:
        return {'estado': 'no_disponible'}

@app.post('/backend/api/jugada')
def recibir_jugada():
    data = request.json
    id_jugador = data['id_jugador']
    id_juego = data['id_juego']
    valor_jugada = data['valor_jugada']

    # Generar el número de la jugada basado en la cantidad de jugadas existentes
    numero_jugada = len(jugadas) + 1

    jugadas.append({
        'id_jugador': id_jugador,
        'id_juego': id_juego,
        'valor_jugada': valor_jugada,
        'numero_jugada': numero_jugada
    })  # Agrega la jugada a la lista de jugadas

    # Agrega la jugada al archivo CSV
    with open('jugadas.csv', 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv)
        writer.writerow([id_jugador, id_juego, valor_jugada, numero_jugada, ''])  # Agrega los datos al archivo CSV

@app.get('/backend/api/juego/resultado')
def obtener_resultado_juego():
    # Realiza el cálculo del resultado del juego y devuelve los datos pertinentes
    # Puedes utilizar los datos almacenados en las listas jugadores y jugadas

    jugadores = ['Jugador 1', 'Jugador 2', 'Jugador 3']  # Ejemplo de jugadores
    valores_jugadas = [random.randint(1, 10) for _ in range(3)]  # Valores de las jugadas aleatorios del 1 al 10
    jugador_ganador = jugadores[valores_jugadas.index(max(valores_jugadas))]  # Jugador con el valor de jugada máximo
    puntaje_acumulado = sum(valores_jugadas)  # Suma de los valores de las jugadas

    return {
        'jugadores': jugadores,
        'valores_jugadas': valores_jugadas,
        'jugador_ganador': jugador_ganador,
        'puntaje_acumulado': puntaje_acumulado
    }

# Resto de las rutas y funciones del servidor...

if __name__ == '__main__':
    # Ejecutar el servidor en el host y puerto especificados
    app.run(host='192.168.231.131', port=8080)

