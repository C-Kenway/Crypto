import socket
import json
from DobladoYSuma import sumar_puntos
from DobladoYSuma import Punto

#HOST = "localhost"
HOST = "192.168.45.165"  # The server's hostname or IP address
PORT = 5000  # Puerto usado por el servidor
buffer_size = 1024

#HOST = str(input('Ingrese el la direccion del host para el server: '))
#PORT = int(input('Ingrese el Puerto: '))
# Crear un objeto socket para el servidor
Bob = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Asignar una dirección IP y un número de puerto al socket
Bob.bind((HOST, PORT))

# Configurar el socket para escuchar conexiones entrantes
Bob.listen(1)
print('El servidor está escuchando en {}:{}'.format(HOST, PORT))

try:
    # Aceptar una conexión entrante
    Alice, direccion = Bob.accept()
    print('Se ha establecido una conexión desde {}:{}'.format(direccion[0], direccion[1]))

    # Recibir valores de la curva elíptica desde el cliente
    aCurva = json.loads(Alice.recv(buffer_size).decode())
    bCurva = json.loads(Alice.recv(buffer_size).decode())
    pModulo = json.loads(Alice.recv(buffer_size).decode())

    # Recibir punto G desde el cliente
    Valores = json.loads(Alice.recv(buffer_size).decode())
    x = Valores[0]
    y = Valores[1]
    G = Punto(x, y)
    print(f"Generador P: {G}")
    ####################################
    # Dato privado Valor de -b- para Bob
    ###################################
    b = 2


    print("En Espera de lo que mande Alice")
    # Recibe el punto generado por alice Punto -A-
    Valores = json.loads(Alice.recv(buffer_size).decode())
    x = Valores[0]
    y = Valores[1]
    A = Punto(x,y)
    print("Punto Recibido Ka: ",A)
    #Nota: b es las veces que debe sumar un punto Bob y la -i- comienza en 0.

    # Para la primera suma
    P = G
    # como -i- comienza en 0 para hacer las iteraciones que sean de bob: es b-1
    for i in range(b - 1):
        P = sumar_puntos(G, P)
    Vx = P.x
    Vy = P.y
    ValPunto = [Vx, Vy]
    Enviar = json.dumps(ValPunto)
    print(f"Punto a enviar Kb: {ValPunto}")
    Alice.sendall(Enviar.encode())

    ####################################
    # Segunda parte: Generar K
    ###################################

    # Para la primera suma
    K = A
    # como -i- comienza en 0 para hacer las iteraciones que sean de Bob es a-1
    for i in range(b - 1):
        K = sumar_puntos(A, K)
    print("Punto K generado para Bob: ", K)

    # Cerrar la conexión con el cliente
    Alice.close()

except Exception as e:
    print("Error:", e)

finally:
    # Cerrar el socket del servidor
    Bob.close()