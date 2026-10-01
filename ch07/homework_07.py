# 3. 다음 함수의 출력 결과를 작성하고, 함수가 어떻게 동작하는지 설명하세요
# def calculate_area(length, width = 10):
#     return length * width
# print(calculate_area(5))
# print(calculate_area(5, 20))

# 4. 다음 코드의 오류 원인을 설명하고, 올바르게 수정하세요.
# def add_numbers(a,b):
#     return a + b

# print(add_numbers(10,5))

# 5. 다음 코드의 출력 결과를 작성하고 동작 내용을 설명하세요.
# def inner_function(x,y):
#     return x + y

# def outer_function(x,y):
#     return inner_function(x,y)
# add_10 = outer_function(10,5)
# print(add_10)

# 6. 오류를 발생시킵니다. 오류 원인을 설명하고 올바르게 수정하세요
# def add_numbers(a, b):
#     result = a + b
#     return result

# print(add_numbers(3,5))

# 7
# def message() :
#     print("A")
#     print("B")
# message()
# print("C")
# message()

# 8
# print("A")
# def message() :
#     print("B")
# print("C")
# message()

# 9. 정수를 매개변수로 입력 받아 해당 정수가 짝수인지 홀수인지 문자열로 반환하는 함수를 작성하세요.
# num = int(input('정수를 입력하시오. 예시(7):'))
# def check_odd_even(num):
#     if num % 2 == 0:
#         result  = '출력: Even'
#     else:
#         result = "출력: Odd"
#     return result
    

# print(check_odd_even(4))
# print(check_odd_even(7))

# 10. 매개변수로 주어진 임의의 숫자 리스트의 평균을 계산하는 프로그램을 작성하시오.

def calculate_average(num_bers_list):
    count = 0
    total = 0
    for num in num_bers_list:
        total += num
        count += 1
    print('총합:',total, '숫자 개수:',count)
    num_avarage = total / count
    print('평균 값:',num)
    return num_avarage

num_list = [10, 20, 30, 40, 50]
avarage = calculate_average(num_list)
print('평균:', avarage)