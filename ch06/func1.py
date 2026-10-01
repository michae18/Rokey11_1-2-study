# func1.py

# 함수 정의
# def 함수명([매개변수]):
#     코드블록
#     [return 반환값]

# 함수 호출
# 함수명(인수1, 이수2, 인수3)

# 사용자 정의 함수
def my_func():
    print('토끼야 안녕!')

# 함수 호출(사용)
my_func()

# def print(매개변수):
#     코드블록
# print(인수)

print('---------------')
na =10
nb =11
nc = na+ nb
print(na,'+',nb, '=',nc)

print('----------------')
def funca(na,nb):
    nc = na +nb
    print(na,'+',nb,'=',nc)
    #[return 반환값]

funca(10,11)

print('----------------')
def add(num1,num2):
    return num1 + num2

print(add(2,3))