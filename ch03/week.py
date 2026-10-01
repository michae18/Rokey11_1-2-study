# input 함수로 문자열 입력, 입력 받은 문자열을 요일 문자열과 비교 연산, 문자열은 따옴표로 표시
print('영어로 변역하고 싶은 요일을 입력(예시: 월요일) ')
yoil = input()

if yoil == '월요일' :
    print('monday')
elif yoil == '화요일' :
    print('tuesday')
elif yoil == '수요일' :
    print('wednesday')
elif yoil == '목요일' :
    print('thursday')
elif yoil == '금요일' :
    print('friday')
elif yoil == '토요일' :
    print('saturday')
elif yoil == '일요일' :
    print('sunday')
else :
    print('잘못 입력하셨습니다.')