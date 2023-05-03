import socket
import time
host ="localhost"
port = 5000
buffer_size=1024
# Creamos un socket para el cliente y establecemos conexion con el servidor
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

#Ubicamos el archivo
filename = 'hamlet.txt'
# Abrimos el archivo
with open(filename, 'rb') as file:
    while True:
        data = file.read(buffer_size)
        if not data:
            break
        try:
            # Enviar datos al servidor
            client_socket.sendall(data)
            time.sleep(0.1)  # Pausa para evitar saturación del socket
        except socket.error:
            pass  # Ignorar errores de no bloqueo

print("Archivo enviado con éxito")

# Cerrar el socket del cliente
client_socket.close()
