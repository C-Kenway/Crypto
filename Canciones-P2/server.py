import socket
import selectors

host = "localhost"
port = 5678
buffer_size = 1024
sel = selectors.DefaultSelector()

def accept(sock):
    conn, addr = sock.accept()
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn):
    datosrecibidos = conn.recv(buffer_size)
    if datosrecibidos:
        file_name = f'AudioRecibido.mp3'
        with open(file_name, 'ab') as f:
            f.write(datosrecibidos)
        print(f"{len(datosrecibidos)} bytes obtenidos y guardados en {file_name}")
    else:
        print("Cliente desconectado")
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind((host, port))
sock.listen()
sock.setblocking(False)
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    events = sel.select()
    for key, _ in events:
        key.data(key.fileobj)