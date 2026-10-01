# 1
# print(3 == 5)

# 2
# print((3 == 3) and (4 != 3))

#3
# if 4 < 3 :
#     print('Hello World.')
# else:
#     print('Hi, there')


#4
# if True :
#       if False:
#           print("1")
#           print("2")
#       else:
#           print("3")
# else :
#       print("4")
# print("5")

#5
# 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하라
# num = int(input("숫자를 입력하시오. :"))

# if num % 2 == 0 :
#     print(num, "짝수입니다")
# else :
#     print(num, '홀수 입니다')
# print("프로그램을 종료합니다.")

#6 
'''사용자로부터 값을 입력 받은 후 해당 값에 20을 더한 값을 출력하라.
 단 사용자가 입력한 값과 20을 더한 계산 값이 255를 초과하는 경우,
 255를 출력해야 한다.
 '''
# num = int(input('숫자를 입력하시오. : '))

# new_num = num + 20

# if num > 255 :
#     print(255)
# elif new_num > 255 :
#     print(255)
# else :
#     print(new_num)

#7.
'''
사용자로부터 하나의 값을 입력받은 후 해당 값에 20을 뺀 값을 출력하라. 
단 출력 값의 범위는 0~255이다. 예를 들어 결과값이 0보다 작은 값이되는 경우 
0을 출력하고 255보다 큰 값이 되는 경우 255를 출력해야 한다.
'''
# num = int(input('숫자를 입력하시오. : '))
# new_num = num - 20

# if num > 255 :
#     print(255)
# elif new_num > 255 :
#     print(255)
# elif new_num < 0:
#     print(0)
# else :
#     print(new_num)

#8 사용자로부터 입력받은 시간이 정각인지 다음과 같이 판별하라.
# time = input("시간을 입력하시오. 예시: 02:00\n")

# hour, minute = time.split(":")

# if minute == "00" :
#     print("정각입니다")
# else:
#     print("정각이 아닙니다")

#9 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
score = int(input('점수를 입력하시오. (예시 :  80) : \n'))

if 100 >= score > 80 :
    print('A')
elif 80 >= score > 60 :
    print('B')
elif 60 >= score > 40 :
    print('C')
elif 40>= score > 20 :
    print('D')
elif 20 >= score >= 0 :
    print('E')
else :
    print('잘못 입력하셨습니다. ')