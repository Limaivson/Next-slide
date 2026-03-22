import socket

host = ''
port = 5000

def send(command: str) -> None:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, port))
    client.send(command.encode())
    client.close()
