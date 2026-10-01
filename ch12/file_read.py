# file_readlines.py

# 파일 열기
f = open(r'ch12\file1.txt','r',
         encoding='utf-8')

# 파일의 전체 내용 읽기
data = f.read()
print(data)
# repr(): 줄바꿈 문자 표시
print(repr(data))

# 파일 닫기
f.close()