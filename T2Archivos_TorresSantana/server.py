import socket
import selectors
host = "localhost"
port = 5000;
# Tamaño del búfer de transferencia
buffer_size=1024
# Crear un nuevo selector
sel = selectors.DefaultSelector()

def read(conn):
    data = conn.recv(buffer_size)
    if data:
        #Obtenemos el puerto de la conexion entrante
        client_port = conn.getpeername()[1]
        # Nombramos el archivo con su puerto
        file_name = f'Recibidox{client_port}.txt'
        # Guardar los datos en el archivo
        with open(file_name, 'ab') as f:
            f.write(data)
        print(f"Recibidos {len(data)} bytes y guardados en {file_name}")
    else:
        print("Cliente desconectado")
        sel.unregister(conn)
        conn.close()


def accept(sock):
    conn, addr = sock.accept()
    print(f"Conexión aceptada desde {addr}")
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host, port))
sock.listen(5)
print(f"Servidor escuchando en {port}")
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

# Bucle principal del servidor
while True:
    events = sel.select()
    for key, _ in events:
        callback = key.data
        callback(key.fileobj)
