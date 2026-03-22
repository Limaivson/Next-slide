import socket
from discovery import find_server

port = 5000

def send(command: str) -> None:
    host = find_server()

    if not host:
        print('Not found')
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        client.send(command.encode())
        client.close()
    except Exception as e:
        print(f'Error connecting: {e}')
