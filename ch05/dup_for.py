# dup_for.py
# 중청 for문

# for 변수 in 리스트
list_j = ["A","B","C","D","E"]

for j in list_j:
    print(j)
    for i in range(10):
        # print(i)
        print('*',end='')
    print('\n')


for num in range(2):
    print(num)