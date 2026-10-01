# file_readlines.py

f = open(r'ch12\file1.txt','r',
         encoding='utf-8')

lines = f.readlines()
# print(lines)
for line in lines:
    print(line, end = '')

f.close()