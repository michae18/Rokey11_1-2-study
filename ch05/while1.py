# while1.py

# (조건식에 사용된) 변수 초기화
# while 조건식:
#     코드블록
#     (while문을 빠져 나올 수 있는) 증감식

for num in range(3):
    print('안녕 거북이', num)


n = 0
while n < 3:
    print('안녕 거북이',n)
    n = n + 1

print('-------------------------')
# while True:
#     print('ctrl + c를 누르세요')

print('----------------------------')
stra = '파이썬'
strb = '프로그래밍'
#stra = stra + strb
stra += strb
print(stra)
# a = a - b
# a -= b

