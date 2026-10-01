# file_open_ex.py
import os

# print('현재 작업공간', os.getcwd())
# file = open(r'ch12\계좌1.txt', 'w', encoding = 'utf-8')
# p1 = '김삿갓 592-89-000089'
# p2 = '이수근 343-64-000064'
# p3 = '박혁거세 136-97-000097'

# file.write('김삿갓 592-89-000089\n')
# file.write('이수근 343-64-000064\n')
# file.write('박혁거세 136-97-000097\n')

# file.close()

path = 'ch12\계좌1.txt'
mode = 'r'
encoding = 'utf-8'
with open(path, mode, encoding=encoding) as file:
    lines = file.readlines()
    # print(lines)
    accountList = []
    for line in lines:
        # print(line[-14:-1])
        accountList.append(line[-14:-1])
print(accountList)


mode = 'r'
with open(path, mode, encoding=encoding) as file:
    lines = file.readlines()
    for number in file:
        # 1. split()함수 활용
        lineList = lines
#         print(number.split(' ')[1])
        # 2. strip()함수 활용
#         양쪽 끝에 있는 공백이나 특정 문자를 제거
#         print(lineList[1].strip())
        accountList.append(lineList[1].strip())
print(accountList)
        