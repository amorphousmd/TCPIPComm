import socket
import time

# Testing tuples
a = [(1, 2), (3, 4), (5, 6)]
b = [(3, 2), (6, 7)]
c = [(1, 5), (9, 4), (2, 6), (6, 7)]
d = []
e = [(1, 5, 0), (9, 4, 0), (2, 6, 0), (6, 7, 0)]


angle = "0"
HOST = '192.168.1.1'
PORT = 5050

def createData(coords_list):
    list1 = [elem for coords in coords_list for elem in coords]
    msg = ""
    for i in list1:
        msg += ","
        msg += str(i)
    msg = str(len(coords_list)) + msg
    return msg


# Socket Setup
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (HOST, PORT)
print('connecting to %s port ' + str(server_address))
s.connect(server_address)

try:
    print("Choose mode:")
    print("1: Text mode")
    print("2: Coordinates mode")
    mode = input("Which mode?")
    try:
        if int(mode) == 1:
            while True:
                msg = input("Send This: ")
                if msg == "quit":
                    break
                s.sendall(bytes(msg, "utf8"))

        elif int(mode) == 2:
            while True:
                s.sendall(bytes(createData(e), "utf8"))
                time.sleep(1)
    except (Exception, ):
        print("Command not recognized")
    finally:
        print("Quitting...")

finally:
    s.close()
