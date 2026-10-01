# select_sort1.py
# 선택 정렬 알고리즘 구현하기 1
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
