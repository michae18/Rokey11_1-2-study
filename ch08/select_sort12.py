# select_sort12.py
# 선택 정렬 알고리즘 구현하기 2
print('---------------------')
ca = [21,10,11,15,13]
mina = ca[0]
minix = 0 
for sb in range(1,5):
    if mina > ca[sb]:
        mina = ca[sb]
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
