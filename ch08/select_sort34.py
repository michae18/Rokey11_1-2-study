# select_sort34.py
# 선택 정렬 알고리즘 구현하기 34
print('---------------------')
ca = [21,10,11,15,13]
mina = ca[0]
minix = 0 
for sb in range(1,5):
    if mina > ca[sb]: # 21 > 10
        mina = ca[sb] # mina = 10
        minix = sb

temp=ca[0]
ca[0] = ca[minix]
ca[minix] = temp
print(ca)

# 1차 목표 ca = [10, 21, 11, 15, 13]

print('---------------------')

mina = ca[1]
minix = 1 
for sb in range(2,5):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

temp=ca[1]
ca[1] = ca[minix]
ca[minix] = temp
print(ca)

# 2차 목표 ca = [10, 11, 21, 15, 13]

print('---------------------')

mina = ca[2]
minix = 2
for sb in range(3,5):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

temp=ca[2]
ca[2] = ca[minix]
ca[minix] = temp
print(ca)

# 3차 목표 = ca = [10, 11, 13, 15, 21]

print('---------------------')

mina = ca[3]
minix = 3
for sb in range(4,5):
    if mina > ca[sb]:
        mina = ca[sb]
        minix = sb

temp=ca[3]
ca[3] = ca[minix]
ca[minix] = temp
print(ca)

# 4 차 목표 = ca = [10, 11, 13, 15, 21]
