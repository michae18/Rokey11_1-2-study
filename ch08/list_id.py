# list_id.py

a = [10, 11, 12, 13]
print('리스트 a:', a)
print('리스트 a id:', id(a))
print('리스트 a[0] id:', id(a[0]))
print('리스트 a[1] id:', id(a[1]))
print('리스트 a[2] id:', id(a[2]))
print('리스트 a[3] id:', id(a[3]))

print('--------------------------')

a[1] = 21
print('리스트 a:', a)
print('리스트 a id:', id(a))
print('리스트 a[0] id:', id(a[0]))
print('리스트 a[1] id:', id(a[1]))
print('리스트 a[2] id:', id(a[2]))
print('리스트 a[3] id:', id(a[3]))

print('--------------------------')
b = a
print('리스트 b:', b)
print('리스트 b id:', id(b))
print('리스트 b[0] id:', id(b[0]))
print('리스트 b[1] id:', id(b[1]))
print('리스트 b[2] id:', id(b[2]))
print('리스트 b[3] id:', id(b[3]))

print('--------------------------')
b = [30,31,32,33]
print('리스트 b:', b)
print('리스트 b id:', id(b))
print('리스트 b[0] id:', id(b[0]))
print('리스트 b[1] id:', id(b[1]))
print('리스트 b[2] id:', id(b[2]))
print('리스트 b[3] id:', id(b[3]))

print('리스트 a:', a)