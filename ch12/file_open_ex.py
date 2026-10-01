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
mode = 'w'
encoding = 'utf-8'
with open(path, mode,encoding = encoding) as file:
    file.write('김삿갓 592-89-000089\n')
    file.write('이수근 343-64-000064\n')
    file.write('박혁거세 136-97-000097\n')

mode = 'r'
with open(path, mode, encoding=encoding) as file:
    for number in file:
        print(number.split(' ')[1])