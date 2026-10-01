# global3.py
b = 0
print('b의 값은',b)
b = 1
print('b의 값은',b)

def scope_test():
    a = 1
    print('함수 내 a 값', a)
    print('함수 내 c 값', c)
    c = 2   # UnboundLocalError
    # UnboundLocalError 에러 발생 이유:
    #  변수 정의 전에 활용해서
    # 같은 지역 사람이 우선 : 함수 내 -  지역 > 전역.

a = 0   # 전역 변수
c = 1   # 전역 변수

print('함수 밖 a 값', a)
print('함수 밖 c 값', c)
scope_test()
print('함수 호출 후 a 값', a)
print('함수 호출 후 c 값', c)