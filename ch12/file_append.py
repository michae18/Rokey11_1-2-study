# file_append.py

# 파일 열기
f = open(r'ch12\file1.txt','a',
         encoding = 'utf-8')

# 파일에 내용 추가
for i in range(11,21):
    data = '%d번째 줄입니다\n' % i
    num = f.write(data)
    print(num)

# 파일 닫기
f.close()