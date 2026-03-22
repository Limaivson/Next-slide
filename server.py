import socket
import threading
import pyautogui

tcp_port = 5000
udp_port = 5001

def discovery_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("", udp_port))

    print('Discovery...')

    while True:
        data, addr = sock.recvfrom(1024)

        if data.decode() == "DISCOVER_SERVER":
            sock.sendto(b"SERVER_HERE", addr)


def tcp_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", tcp_port))
    server.listen()

    print('Server found')

    while True:
        conn, addr = server.accept()
        data = conn.recv(1024).decode()

        print(f"Comando recebido: {data}")

        if data == "next":
            pyautogui.press("right") # Next slide
        elif data == "prev":
            pyautogui.press("left") # Prev slide

        conn.close()


threading.Thread(target=discovery_server, daemon=True).start()
tcp_server()