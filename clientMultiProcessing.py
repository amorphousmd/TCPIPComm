import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connected = False
sendDataOrder = False
closeClientOrder = False

dataBuffer = ''
e = [(1, 5, 0), (9, 4, 0), (2, 6, 0), (6, 7, 0)]


def startClient():
    # HOST = '192.168.1.1'
    HOST = '127.0.0.1'
    PORT = 5050
    server_address = (HOST, PORT)
    print(f'[CONNECTING] TO PORT: {server_address}')
    try:
        clientSocket.connect(server_address)
    except ConnectionRefusedError:
        print("No server found")
    else:
        global connected
        connected = True
        while True:
            global sendDataOrder
            global closeClientOrder
            if sendDataOrder:
                global dataBuffer
                clientSocket.sendall(bytes(dataBuffer, "utf8"))
                dataBuffer = ''
                sendDataOrder = False
            if closeClientOrder:
                closeClientOrder = False
                clientSocket.close()


def createData(coords_list):
    list1 = [elem for coords in coords_list for elem in coords]
    msg = ""
    for i in list1:
        msg += ","
        msg += str(i)
    msg = str(len(coords_list)) + msg
    return msg


def sendCoordinates(inputCoords):
    if connected:
        global dataBuffer
        dataBuffer = createData(inputCoords)
    else:
        print("Socket not connected")


def closeClient():
    global closeClientOrder
    closeClientOrder = True

