import socket
puerto = 1337 # Cada que le hablen al puerto redirigelo a este socket.

# Especificar protocolo del socket (capa 3 y capa 4)
# SOCK_STREAM es TCP y SOCK_DGRAM es UDP.
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Poner a escuchar un puerto
# 0.0.0.0 significa cualquier interfaz de la computadora.
s.bind(("0.0.0.0", puerto))

# Solo escuchar a una conexion
s.listen(1)

# Aceptar que alguien se conecte
# Regresa el socket donde se va a recibir y enviar informacion y la direccion de quien se conecto.
conn, addr = s.accept()

with conn:
    # De la conexion se van a recibir hasta 1024 bytes
    data = conn.recv(1024)
    print(data.decode("ascii"))
    conn.send(b"hola")
    conn.close()