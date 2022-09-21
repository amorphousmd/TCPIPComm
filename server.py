# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(5)  # A queue of 5
#
# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established")
#     clientsocket.send(bytes("Welcome to the server", "utf-8"))  # Local version of clientsocket

import socket


HOST = '192.168.1.1'
PORT = 5050

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2)

while True:
    client, addr = s.accept()

    try:
        print('Connected by', addr)
        while True:
            data = client.recv(1024)
            str_data = data.decode("utf8")
            if str_data == "quit":
                break

            print("Client: " + str_data)

    finally:
        s.close()
        break