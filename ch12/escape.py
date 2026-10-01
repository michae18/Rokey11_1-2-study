# escape.py

# 이스케이프(escape) 코드: 미리 정의해둔 문자 조합
# \n = new line = LF(line feed)
# '\t' = tab
# '\b' = backspace : 하나 지우기
# "\'" = 작은 따음표 표시할 때          '안녕 난 \'민\'이라고 해'
# "\"" = 큰 따음표 표시
# '\\' = 역슬레쉬 표시
# "\r" = CR(carrige return)       # 커서를 현재 줄 가장 앞으로 이동
# 그 외에도 form feed('\f'), verticla Tab('\t') 등등

print('hello\t world\n')
#repr(): 객체를 개발자가 확인하기 좋은 문자열로 표현
#print(repr('hello\t world\n))
print('hi', end = '\b')
print('kenneth \'lim\'', end='')
print('\rthanks')

str1 = 'test\b'
str2 = 'test'

str3 = str1 + str2
print(str3)
print(len(str3))

  


# 다양한 파일 처리 모드
# 'r' : read
# 'w' : write
# 'a' : append()
# 'r+' : read + write => 파일을 읽고 쓰기(기 데이터 존재)
# 'w+' : write + read => 파일을 새로 만들거나 비우고 쓰고 읽기
#  'a+' : append + read