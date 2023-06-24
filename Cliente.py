import requests  # Importar el módulo 'requests' para realizar solicitudes HTTP

def ingresar_id_jugador():
    id_jugador = input("Ingrese el ID del jugador: ")  # Solicitar al usuario que ingrese el ID del jugador
    return id_jugador

def ingresar_id_juego():
    id_juego = input("Ingrese el ID del juego: ")  # Solicitar al usuario que ingrese el ID del juego
    return id_juego

def consultar_juego_disponible():
    response = requests.get("http://192.168.1.185:8080/backend/api/juego/disponible")
    # Realizar una solicitud GET a la URL especificada para consultar si hay un juego disponible
    data = response.json()  # Obtener los datos de la respuesta en formato JSON

    if data["estado"] == "disponible":  # Comprobar si el estado del juego es "disponible"
        print("Juego disponible")
        print("ID del juego en curso:", data["id_juego"])  # Mostrar el ID del juego en curso
    else:
        print("No hay juego disponible en este momento")

def realizar_jugada():
    id_jugador = ingresar_id_jugador()  # Llamar a la función para ingresar el ID del jugador
    id_juego = ingresar_id_juego()  # Llamar a la función para ingresar el ID del juego
    valor_jugada = input("Ingrese el valor de la jugada: ")  # Solicitar al usuario que ingrese el valor de la jugada

    payload = {
        "id_jugador": id_jugador,
        "id_juego": id_juego,
        "valor_jugada": valor_jugada
    }

    response = requests.post("http://192.168.1.185:8080/backend/api/jugada", json=payload)
    # Realizar una solicitud POST a la URL especificada con los datos de la jugada
    if response.status_code == 200:  # Comprobar si la solicitud fue exitosa (código de estado 200)
        print("Jugada realizada con éxito")
    else:
        print("Error al realizar la jugada")

def consultar_resultado_juego():
    response = requests.get("http://192.168.1.185:8080/backend/api/juego/resultado")
    # Realizar una solicitud GET a la URL especificada para consultar el resultado del juego
    data = response.json()  # Obtener los datos de la respuesta en formato JSON

    print("Nombre de los jugadores:", data["jugadores"])  # Mostrar los nombres de los jugadores
    print("Valores de las jugadas:", data["valores_jugadas"])  # Mostrar los valores de las jugadas
    print("Jugador ganador:", data["jugador_ganador"])  # Mostrar el jugador ganador
    print("Puntaje acumulado de los jugadores:", data["puntaje_acumulado"])  # Mostrar el puntaje acumulado de los jugadores

# Menú principal
while True:
    print("----- MENU -----")
    print("1. Ingresar ID del jugador")
    print("2. Ingresar ID del juego")
    print("3. Consultar juego disponible")
    print("4. Realizar jugada")
    print("5. Consultar resultado del juego")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")  # Solicitar al usuario que seleccione una opción del menú

    if opcion == "1":
        id_jugador = ingresar_id_jugador()  # Llamar a la función para ingresar el ID del jugador
        print("ID del jugador ingresado:", id_jugador)  # Mostrar el ID del jugador ingresado
    elif opcion == "2":
        id_juego = ingresar_id_juego()  # Llamar a la función para ingresar el ID del juego
        print("ID del juego ingresado:", id_juego)  # Mostrar el ID del juego ingresado
    elif opcion == "3":
        consultar_juego_disponible()  # Llamar a la función para consultar el juego disponible
    elif opcion == "4":
        realizar_jugada()  # Llamar a la función para realizar una jugada
    elif opcion == "5":
        consultar_resultado_juego()  # Llamar a la función para consultar el resultado del juego
    elif opcion == "6":
        print("Saliendo del programa...")
        break  # Salir del bucle y finalizar el programa
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

