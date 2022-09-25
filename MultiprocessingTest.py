import time
from multiprocessing import Process
from multiprocessing import Pipe
import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendDataOrder = False
connected = False
dataBuffer = ''
e = [(1, 5, 0), (9, 4, 0), (2, 6, 0), (6, 7, 0)]



def createData(coords_list):
    list1 = [elem for coords in coords_list for elem in coords]
    msg = ""
    for i in list1:
        msg += ","
        msg += str(i)
    msg = str(len(coords_list)) + msg
    return msg


def function():
    global sendDataOrder
    sendDataOrder = True


def sendCoordinates(inputCoords):
    if connected:
        global dataBuffer
        dataBuffer = createData(inputCoords)
    else:
        print("Socket not connected")


def closeClient():
    global closeClientOrder
    closeClientOrder = True


# generate work
def sender(connection):
    print('Sender: Running', flush=True)
    # print(sendDataOrder)
    if sendDataOrder:
        connection.send(1)

def getvalue():
    print(sendDataOrder)


# While loop to not lose connection with server
def receiver(connection):
    # HOST = '192.168.1.1'
    HOST = '127.0.0.1'
    PORT = 5050
    server_address = (HOST, PORT)
    print(f'[CONNECTING] TO PORT: {server_address}')
    clientSocket.connect(server_address)
    while True:
        if connection.recv() == 1:
            clientSocket.sendall(bytes("dasdasdh", "utf8"))
            time.sleep(1)
    # try:
    #     clientSocket.connect(server_address)
    # except ConnectionRefusedError:
    #     print("No server found")
    # else:
    #     print("Here")
    #     while True:
    #         print(connection.recv())
    #         clientSocket.sendall(bytes("dasdasdh", "utf8"))
    #         time.sleep(1)
    #         pass


# entry point
def clientStart():
    # start the sender
    pass
    # start the receiver


# Testing section
if __name__ == '__main__':
    clientStart()
    sendDataOrder = True
    conn1, conn2 = Pipe(duplex=True)
    receiver_process = Process(target=receiver, args=(conn1,))
    receiver_process.start()
    sender_process = Process(target=sender, args=(conn2,))
    sender_process.start()
    while True:
        getvalue()
        time.sleep(1)