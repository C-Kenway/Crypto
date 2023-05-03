import socket
import json
from DobladoYSuma import sumar_puntos
from DobladoYSuma import Punto
from DobladoYSuma import verificar
import os
#HOST = "127.0.0.1"  # Nombre del host o direccion ip
HOST = "192.168.197.25"  # Nombre del host o direccion ip
PORT = 5000  # Puerto usado por el servidor
buffer_size = 1024

#HOST = str(input('Ingrese el la direccion del host para el server: '))
#PORT = int(input('Ingrese el Puerto: '))
# Crear un objeto socket para el cliente (Alice)
Alice = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectar el socket a un servidor remoto en el puerto 5000
Alice.connect((HOST, PORT))
print('Se ha establecido una conexión con el servidor remoto.')


#Aqui comineza el programa

####################################
#Datos Publicos
###################################

print("Notacion: y^2 = x^3 + ax + b (mod p):")
# Definimos los valores de 'a' como -aCurva-, 'b' como -bCurva- y 'p' como -pModulo- para la curva elíptica
#Valor a
#Ingresa el valor para "a" en la expresion de la formula
aCurva=int(input("Ingrese l valor de a: \n"))
eleccion = str(aCurva)
Alice.send(eleccion.encode())
#Ingresa el valor para "b" en la expresion de la formula
bCurva=int(input("Ingrese l valor de b: \n"))
eleccion = str(bCurva)
Alice.send(eleccion.encode())
#Ingresa valor de Modulo
pModulo=int(input("Ingrese l valor de p: \n"))
eleccion = str(pModulo)
Alice.send(eleccion.encode())
while(True):
    print("Notacion: Punto[Valor X, Valor Y]")
    # Generador
    # Valor x
    Gx = int(input("Ingrese el Valor X: \n"))
    # Valor y
    Gy = int(input("Ingrese el Valor Y: \n"))
    G = Punto(Gx,Gy)
    # Verificamos si el punto G es generador su no entonces no continua
    ver = verificar(aCurva, bCurva, pModulo, G)
    if ver == 1:
        Vx = G.x
        Vy = G.y
        ValPunto = [Vx, Vy]
        Enviar = json.dumps(ValPunto)
        Alice.sendall(Enviar.encode())
        break
    else:
        print(f"El punto P: {G}. No es generador en la curva intente otros valores")



####################################
#Dato privado Valore de -a- para Alice: Esta es tambien las veces que debe sumar el punto generador
###################################
a=3

#Nota: a es las veces que debe sumar un punto Alice y la i comienza en 0.

# Para la primera suma
P = G
# como i comienza en 0 para hacer las iteraciones que sean de alice es a-1
for i in range(a - 1):
    P = sumar_puntos(G, P)
Vx = P.x
Vy = P.y
ValPunto = [Vx, Vy]
print(f"Alice envia :{ValPunto}")
Enviar = json.dumps(ValPunto)

Alice.sendall(Enviar.encode())

print("En espera de lo que mande Bob")
# En espera del punto -B- de Bob
Valores = json.loads(Alice.recv(buffer_size).decode())
x = Valores[0]
y = Valores[1]
B = Punto(x, y)
print("Punto Recibido DE Bob", B)

####################################
#Segunda parte: Generar K
###################################

# Para la primera suma
K = B
# como i comienza en 0 para hacer las iteraciones que sean de alice es a-1
for i in range(a - 1):
    K = sumar_puntos(B, K)
print("Punto K generado para Alice: ",K)
# Cerrar la conexión con el servidor
Alice.close()

