# pinput.py

print('첫 번째 정수 입력:')
ra = input()
rb = input('두 번째 정수 입력:')
rc = ra + rb
print(ra, '+', rb, '=', rc) # 결과 값: 205

# 숫자 + 숫자 = 덧셈 결과
# 문자열 + 문자열 = 연결된 문자열

# 문제 => 덧셈을 하고 싶으나 자료형이 맞지 않음
# 해결 방법 => 문자열 => 정수형 변환 : int()

print('-----------------------------------------')

print('첫 번째 정수 입력:')
ra = input()
rb = input('두 번째 정수 입력:')
print(type(ra))         # str, "20"
print(type(rb))         # str, "5"

# int(데이터): 정수형으로 변환
# float(데이터): 실수형으로 변환
# str(데이터): 문자열으로 변환
# 변환된 값은 리턴 값이 있다.
# 문자열을 정수로 변환
ra = int(ra)        # str => int, "20" => 20
rb = int(rb)        # str => int, "5" => 5
rc = ra + rb
print(ra, '+', rb, '=', rc) # 결과 값: 205
print(type(rc))