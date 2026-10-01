# p1.py

x = 10
def fadd(num):
    b = x + num
    print('변수 x값은',x)
    print('변수 b값은',b)
fadd(10)

print('------------------------')
def fadd(num):
    # 해결방법 1 : 지역변수 선언
    # x = 1
    # 해결방법 2 : global 변수 사용
    global x
    x = x + num         # UnboundLocalError
    print('변수 x값은', x)

fadd(10)

print('------------------------')
def fadd(num):
    global x
    x = x + num
    print('변수 x값은', x)

print('--------------------------')

price = int(input('현재 가격:'))

def print_lower_price(num):
    disc_price = int(price * 0.9)
    return disc_price

final_price = int(print_lower_price(price))
print(final_price)
 