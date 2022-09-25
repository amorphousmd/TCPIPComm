import time

from MultiprocessingTest import *

if __name__ == '__main__':
    clientStart()
    time.sleep(2)
    a = input('Input something: ')
    print(a)
    global sendDataOrder
    print(sendDataOrder)
    sendDataOrder = True
    print(sendDataOrder)
    print('done')