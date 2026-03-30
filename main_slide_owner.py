from server import discovery_server, tcp_server
import threading

threading.Thread(target=discovery_server, daemon=True).start()
tcp_server()
