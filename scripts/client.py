import socket

# Crear el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecer la ip y el puerto al que se va a conectar
s.connect(("10.49.32.215", 1337))

# Enviar el texto
s.send(b"Desde el cliente")

data = s.recv(1024)
print(data.decode("ascii"))
s.close()