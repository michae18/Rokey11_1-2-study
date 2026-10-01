# # def welcome():
# #     print('이상한 나라에 오신 것을 환영합니다')

# # welcome()

# # def welcome(name):
# #     print(name, '님 이상한 나라에 오신 것을 환영합니다')

# # welcome('앨리스')
# # welcome('도도새')

# def draw_stars(num):
#     print('*' * num)
# draw_stars(2)

# for i in range(3,0,-1):
#     print('*' * i)

# print('-------------------------')

# num1 = int(input('숫자1을 입력하시오. :'))
# num2 = int(input('숫자2을 입력하시오. :'))

# def fadd(num1, num2):
#     result = num1 + num2
#     print(result)
#     return result

# def fsub(num1, num2):
#     result = num1 - num2
#     print(result)
#     return result

# def fmul(num1, num2):
#     result = num1 * num2
#     print(result)
#     return result

# def fdiv(num1, num2):
#     result = num1 / num2
#     print(result)
#     return result


# def calculate(num1, num2):
#    fadd(num1, num2)
#    fsub(num1, num2)
#    fmul(num1, num2)
#    fdiv(num1, num2)

# calculate(num1,num2)

print('-------------------------------')
# stra = 'python example'
# def string_length(str):
#     count = 0
#     for string in stra:
#         count +=1
#         print(string,count)
#     return count

# lena = string_length(stra)
# print('문자열 길이 :',lena)

# num1 = int(input('숫자를 입력하세요: '))
# num2 = int(input('숫자를 입력하세요: '))

# def fdiv(num1,num2):
#     if num2 == 0:
#         print('0으로 나눌 수 없다')
#     else:
#         result = num1 / num2
#         return result

# print(fdiv(num1,num2))

num = int(input('숫자를 입력하시오.: '))
def find_num_mul(int):
    result = 0
    for number in range(1,101):
        if number % num == 0:
            result += number
        else :
            continue
    return result

print(find_num_mul(num))