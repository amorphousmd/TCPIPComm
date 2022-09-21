a = [(1, 2), (3, 4), (5, 6)]
b = [(3, 2), (6, 7)]
c = [(1, 5), (9, 4), (2, 6), (6, 7)]
d = []

def createData(coords_list):
    list1 = [elem for coords in coords_list for elem in coords]
    msg = ""
    for i in list1:
        msg += ","
        msg += str(i)
    msg = str(len(coords_list)) + msg
    return msg

print(createData(a))
print(createData(b))
print(createData(c))
print(createData(d))