import socket

UDP_PORT = 5001

def find_server(timeout=3):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.settimeout(timeout)

    try:
        sock.sendto(b"DISCOVER_SERVER", ("255.255.255.255", UDP_PORT))
        data, addr = sock.recvfrom(1024)

        if data.decode() == "SERVER_HERE":
            return addr[0]

    except:
        return None