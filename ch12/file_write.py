# file_write.py

# f = open(r'ch12\file1.txt', 'w', encoding='cp949')
f = open(r'ch12\file1.txt', 'w', encoding='utf-8')

# f.write('1번째 줄입니다.')
for i in range(1,11):
    data = '%d번째 줄입니다\n' % i
    f.write(data)

f.close()