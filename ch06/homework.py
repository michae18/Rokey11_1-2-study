# homework.py

# 5. "안녕하세요" 문자열을 화면에 출력하는 print_hello() 함수를 정의하시오. 
# string = '안녕하세요'
# def print_hello(str) :
#     print(string)
#     return

# 6. 앞서 정의한 print_hello() 함수를 호출하시오.
# print_hello(string)

# # 7. 앞서 정의한 print_hello() 함수를 100번 호출하시오.
# for repeat_number in range(101):
#     print_hello(string)
# print(repeat_number)

# 8. 다음과 같이 출력하는 greet() 함수를 정의하고 호출하시오. 
# (단, 매개변수 name의 기본 값으로 Guest를 출력할 것.)
# Hello, Alice!
# insert_name = input('이름을 입력하세요. :')
# def greet():
#     name = 'Guest'
#     if insert_name == '\n':
#         pass
#     else :
#         name = insert_name

#     print('Hello,', name)
# greet()

def multiply(a, b):
    result = a* b
    return result

print(multiply(4,5))