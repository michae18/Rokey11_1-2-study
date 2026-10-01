# select_sort12.py
# 선택 정렬 알고리즘 구현하기 6
# 함수 정의 및 호출

# def fselsort(매개변수):
#     반복 코드 
#     return 반환값

def fselsort(ca):
    for sa in range(0,4) : 
        mina = ca[sa]
        minix = sa 
        for sb in range(sa+1,5,1):
            if mina > ca[sb]: # 21 > 10
                mina = ca[sb] # mina = 10
                minix = sb

        ca[sa], ca[minix] = ca[minix] , ca[sa]  
        print(ca)
    return ca
print('---------------------')
ca = [21,10,11,15,13]
print(fselsort(ca))
print(ca)