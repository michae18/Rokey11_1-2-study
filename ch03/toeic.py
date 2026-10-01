tscore = int(input('점수를 입력하세요: '))

# if tscore > 900 :
#     print('토익 점수: ',tscore,' 상위권')
# elif 900 >= tscore > 700 :
#     print('토익 점수: ',tscore,' 중위권')
# else :
#     print('토익 점수: ',tscore,' 하위권')
# print('프로그램을 종료합니다')

if tscore > 900 :
    print('토익 점수: ', tscore, '상위권')
elif 900 >= tscore > 600 :
    print('토익 점수: ',tscore,' 중상위권')
elif 600 >= tscore > 300 :
    print('토익 점수: ',tscore,' 중위권')
else :
    print('토익 점수: ',tscore,' 하위권')
print('프로그램을 종료합니다')