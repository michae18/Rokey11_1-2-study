# global3.py
b = 0
print('b의 값은',b)
b = 1
print('b의 값은',b)

def scope_test():
    # 방법 1 : a = 1, 지역 변수 
    # 방법 2 : global 함수 사용하여 전역 변수 사용
    # 1. a = 1
    # 2. global a 
    #  둘 중 하나 사용
    # a = 1
    global a
    a = a + 3   # 지역 변수 할당 필요
    print('함수 내 a 값', a)

a = 0
print('함수 밖 a 값', a)
scope_test()
print('함수 호출 밖 a 값', a)