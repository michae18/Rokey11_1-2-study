# list_id2.py

def fk(cb):
    total = 0
    for sb in range(0,3,1):
        total = total + cb[sb]
    cb[2] = total
    return cb


ca = [10, 20, 30]
print(ca)
print(id(ca))
print('리스트 a[0] id:', id(ca[0]))
print('리스트 a[1] id:', id(ca[1]))
print('리스트 a[2] id:', id(ca[2]))

cd = fk(ca)
print(ca)
print(id(ca))
print('리스트 a[0] id:', id(ca[0]))
print('리스트 a[1] id:', id(ca[1]))
print('리스트 a[2] id:', id(ca[2]))

print(cd)
print(id(cd))
print('리스트 a[0] id:', id(cd[0]))
print('리스트 a[1] id:', id(cd[1]))
print('리스트 a[2] id:', id(cd[2]))