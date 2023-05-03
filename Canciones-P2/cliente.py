import socket
from datetime import time

host = "localhost"
port = 5678
buffer_size = 1024

client_socket = socket.socket()
client_socket.connect((host, port))

filename = 'audio.mp3'
with open(filename, 'rb') as file:
    while True:
        data = file.read(buffer_size)
        if not data:
            break
        try:
            # Enviar datos al servidor
            client_socket.sendall(data)
        except socket.error:
            pass  # Ignorar errores de no bloqueo
        time.sleep(0.1)  # Agregar una pausa de 0.1 segundos

client_socket.close()