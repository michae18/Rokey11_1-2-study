# break1.py
# 반복을 종료
count = 0 
while count < 3:
    count = count + 1
    if count == 2:
        break
    print(count)
print('반복문 종료')

print('---------------------------')

users = ['kim', 'lee', 'park']

for user in users:
    if user == 'lee':
        print('발견')
        break
