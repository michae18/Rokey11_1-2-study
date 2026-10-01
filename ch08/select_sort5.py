# select_sort12.py
# 선택 정렬 알고리즘 구현하기 5
print('---------------------')
ca = [21,10,11,15,13]

for sa in range(0,4) : 
    mina = ca[sa]
    minix = sa 
    for sb in range(sa+1,5,1):
        if mina > ca[sb]: # 21 > 10
            mina = ca[sb] # mina = 10
            minix = sb

    temp=ca[sa]
    ca[sa] = ca[minix]
    ca[minix] = temp
    print(ca)

# def fselsort(매개변수):
#         코드블록
#     return 결과값