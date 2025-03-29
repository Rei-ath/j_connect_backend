import socket
import select
import time
from consts import *

def main_tcp_socket(address='du ip?', port=42069):
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_socket.bind((address, port))
    tcp_socket.listen(5)
    print(f'Vrooom vrooom on {tcp_socket.getsockname()}')

    # Create a list to keep track of all connected clients
    client_sockets = [tcp_socket]

    while True:
        try:
            # Use select to monitor sockets for activity
            readable, _, _ = select.select(client_sockets, [], [])
            for sock in readable:
                if sock is tcp_socket:
                    # New client connection
                    cs, addr = sock.accept()
                    print(f"Connection from {addr} established vrooom room")
                    client_sockets.append(cs)
                else:
                    # Data from an existing client
                    data = sock.recv(1024)
                    if len(data) != 0:
                        data = data.decode("utf-8")
                        print(f"Received data from {sock.getpeername()}: {data}")
                        if data in EVENTS_VALS:
                            try:
                                event = EVENTS_VALS[data]
                                print("EVENTS_VALS[data]",event)
                                event_in_bytes  = event.to_bytes(1, byteorder='big')
                                if len(event_in_bytes)==1:
                                    cs.sendall(event_in_bytes)
                                    time.sleep(.1)
                            except Exception as e:
                                print("just a scratch",e)

        except KeyboardInterrupt:
            for cs in client_sockets:
                cs.close()
            tcp_socket.close()

if __name__ == '__main__':
    try:
        main_tcp_socket()
    except Exception as e:
        print("just a scratch",e)
