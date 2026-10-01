# find_max.py

print('1------------------')
# 최대값 찾기
ca = [10, 13, 17, 11]
max = ca[0]
if max < ca[1]:
    max = ca[1]
    print(id(max))
if max < ca[2]:
    max = ca[2]
    print(id(max))
if max < ca[3]:
    max = ca[3]
    print(id(max))
print(id(max),max)

print('2---------------------')

ca = [10, 15, 18, 11]
max = ca[0]
print(id(max))

for sb in range(1, 4, 1):
    if max < ca[sb] :
        max = ca[sb]
        print(id(max),max)

print(id(max),max)

print('2---------------------')

ca = [10, 17, 13, 11]
max = ca[0]

for sb in ca:
    if max < sb:
        max = sb
        print(id(max),max)
print(id(max),max)