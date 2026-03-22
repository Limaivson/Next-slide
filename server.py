import socket
import pyautogui

host = '0.0.0.0'
port = 5000

server = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

print('Server on')

while True:
    conn, addr = server.accept()
    data = conn.recv(1024).decode()

    if data == "next":
        pyautogui.press("right") # Next slide
    elif data == "prev":
        pyautogui.press("left") # Prev slide

    conn.close()