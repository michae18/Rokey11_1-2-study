# file_open_ex3.py
path = r'ch12\계좌1.txt'
mode = 'r'

with open(path,mode,encoding='utf-8') as f:
    lines = f.readlines()
    accountDict = {}

    for line in lines:
        lineList = line.split(' ')
        accountDict[lineList[0]] = lineList[1].strip()
        # print(lineList[0])
        # print(lineList[1].strip())

# print(accountDict)
for key, val in accountDict.items():
    print(key, ':', val)