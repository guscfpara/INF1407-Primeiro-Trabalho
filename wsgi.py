import web_server
import threading
from socket import socket, AF_INET, SOCK_STREAM
from configs import web_server_config
from web_server import client_request

if __name__ == '__main__':
    # Server Port
    server_port = web_server_config['port']

    # Create a clientless server socket
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(('', int(server_port)))
    tcp_socket.listen(0)

    print(f'Access url : http://localhost:{server_port}')

    # Program waits for a connection
    while True:
        # When receiving a connection, returns a socket with client, server and client address, creating a Thread
        connection, client = tcp_socket.accept()
        new_thread = threading.Thread(group=None, target=client_request, args=(connection, client, web_server_config))
        new_thread.start()