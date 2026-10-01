# global2.py
b = 0
print('b의 값은',b)
b = 1
print('b의 값은',b)

def scope_test():
    global a
    a = 1   # 전역 변수
    print('scope_test() 함수 안의 a 값은', a)   # 출력 순서: 2번

a = 0
print('scope_test() 함수 밖의 a 값은', a)       # 출력 순서: 1번
scope_test()
print('scope_test() 함수 호출 후 a 값은', a)    # 출력 순서: 3번