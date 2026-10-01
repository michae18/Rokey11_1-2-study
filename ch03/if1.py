# if1.py

## if문

# if 조건식: 
#    코드블록
# print('프로그램 시작')
# a = 10
# if a> 11:
#     print('참입니다')
# else:
#     print('거짓입니다')

print('---------------------------')
# score = 90      # 초기화0
# # score = 70      # 재 할당
# if score > 80:
#     print('점수 :', score)
#     print('합격입니다')
# print('프로그램 종료합니다')

print('----------------------------------\n')

# if- else문
'''
if 조건식:
    코드블록1
else:
    코드블록2
'''
# score = 60
# print('점수: ',score)
# if score > 80:
#     print('합격입니다.')
# else:
#     print('불 합격입니다.')
# print('프로그램을 종료합니다.')

print('----------------------------')

# if-elif-else 문
'''if 조건문:
    코드블록1
elif 조건문:
    코드블록2
else :
    코드블록3
'''
# score = 70
# if score >= 70:
#     print('A')
# elif score <= 70:
#     print('B')
# else:
#     print('D')


# if-elif 문 (else 없이 사용 가능)
'''
if 조건식:
    코드블록1
elif 조건식:
    코드블록2
'''

print('-------------------------------')

# 동작 내용: 짝수 판별
# na = 21
# if na / 2 == 0:         # na를 2로 나눈 나머지가 0인지 판단
#     print(na,'짝수')    # 참일때, na 값과 '짝수' 문자열 출력
# else:
#     print(na ,'홀수')
# print('if문 종료됨')

print('-----------------------------------')

# 동작 내용: 짝수와 홀수를 확인하되,
# 0인 경우도 함께 판별하여 출력하기

num = 0
# if score == 0:
#     print(score,'zero')
# elif score % 2 == 0:
#     print(score, '짝수입니다')
# else :
#     print(score, '홀수입니다')
# print('if문 종료')

# if score % 2  ==0:
#     if score == 0:
#         print(score,'zero')
#     print(score,'짝수입니다')
# else :
#     print(score, '홀수입니다')
# print('if문 종료')

# score = 0.0
# if score % 2 == 0:
#     print(score,'짝수입니다')
# elif score % 2 != 0:
#     print(score, '홀수입니다')
# else :
#     print('zero')
# print('if문 종료')

print('--------------------------------')


num = input('점수를 입력하시오. :')
print(type(num))
if num == '0':
    print('zero')
    num = int(num)
    print(type(num))
elif num % 2 == 0 :
    print(num, '짝수')
elif num % 2 != 0 :
    print(num, '홀수')
print('프로그램을 종료합니다')

