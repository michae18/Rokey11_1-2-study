# weekend_homework.py
# 2.1
# a = 3.14
# b = True
# c = 'False'
# abc_types = [a, b, c]
# for types in abc_types:
#     print(type(types),end=' ')

# 2.2
# num1 = int(input('숫자1을 입력하시오.: '))
# num2 = int(input('숫자2을 입력하시오.: '))
# print('덧셈  ',   num1,' + ',num2, ' = ',num1 + num2 )
# print('뺄셈  ',   num1,' - ',num2, ' = ',num1 - num2 ) 
# print('곱셈  ',   num1,' * ',num2, ' = ',num1 * num2 ) 
# print('나눗셈', num1,' / ',num2, ' = ',num1 / num2 ) 

# 3.1
# water = 700
# if water >= 1000:
#     print('충분')
# elif water < 1000 and water >= 500 :
#     print('적절')
# else:
#     print('부족')

# 3.2
# score = int(input('숫자를 입려하시오. : '))
# if score > 90 :     print('A학점')
# elif 90 > score >= 80 :    print('B학점')
# elif 80 > score >= 70 :    print('C학점')
# else:    print('F학점')

# # 4.1
# fruits = ['banana','peach','lemon', 'grape']
# print(fruits[2])

# 4.2
# studente3 = {'나이' : 22, '직업' : '학생', '취미' : '게임'}
# studente3['도시'] = '수원'
# print(studente3)

# 5.1
# Number = [1,2,3,4,5]
# for num in Number:
#     print(num,end = ' ')

# 5.2
# fruits = ['바나나', '파인애플', '복숭아','사과','포도']
# time = 0
# for fruit in fruits:
#     if fruit == '사과' :
#         print(time,'번째' '사과를 찾았습니다')
#     else:
#         time += 1

# 6.1
# a = int(input('숫자를 입력하시오. :'))
# b = int(input('숫자를 입력하시오. :'))
# def solution(a, b):
# 		sum = a + b
# 		sub = a - b
# 		multi = a * b
# 		return sum, sub, multi
# print(solution(a, b))

# 6.2
num = int(input('숫자를 입력하시오. :'))
def add_num(num) :
	total = 0
	for number in range(1,num + 1):
		total = total + number
	return total

print(add_num(num))