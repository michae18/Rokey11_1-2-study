# swap.py
# 변수 간 데이터 스왑1
na = 10
nb =11
print('na:', na, 'nb:',nb)
temp =na
na = nb
nb = temp
print('na:', na, 'nb:',nb)

print('------------------------------')
# 변수 간 데이터 스왑 2
na = 10
nb =11
print('na:', na, 'nb:',nb)
na,nb = nb , na
print('na:', na, 'nb:',nb)

print('------------------------------')
# 함수 내 데이터 스왑 시도
def funca(pa,pb): # pa,pb : 지역 변수
    temp = pa   # temp: 지역 변수
    pa = pb     
    pb = temp   

na = 10 # 전역 변수
nb =11  # 전역 변수
print('na:', na, 'nb:',nb)
funca(na, nb)
print('na:', na, 'nb:',nb)

# print(pa) # NameError : 정의 된적 없음(funca의 지역변수)

print('------------------------------')
# 함수 사용 데이터 스왑
# 문제: na와 nb를 스완하는 함수를 작성시오.

def funca(pa,pb) :
    temp = pa   # temp = 10
    pa = pb     # pa = 11 
    pb = temp   # pb = 10
    return pa,pb

na = 10
nb = 11
# result = funca(na,nb)
# print('result:',result,type(result))
na, nb = funca(na,nb)   # 언패킹 (unpacking)
print('na:', na, 'nb:',nb)