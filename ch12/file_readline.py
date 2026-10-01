# file_readline.py

f = open(r'ch12\file1.txt','r',
         encoding = 'utf-8')

line = f.readline()
print(line)
line = f.readline()
print(line)

f.close()

# # 다음 코드는 키워드의 사용 불가
# (method) def readline(
#     size: int = -1,
#     /          # 위치 인수만 사용 가능
# ) -> str