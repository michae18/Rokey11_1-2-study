# continue1.py
# 일부 코드를 제외하고 반복
# count = 0

# while 조건식:
#     코드블록
#     count 증감식

count = 0       # 1 2 3

while count < 3:
    count += 1
    if count == 2:
        continue
    print(count)

print('---------------------')
# 필터링 예제
# ''빈 값 / None => 건너뜀
# 유효한 데이터만 처리
users = ['admin', 'guest', 'user1', None,1,1.08 ,2>4, '']
print(users)

for user in users :
    if not user:
        continue
    print(user)

# 표현  자료형      의미
# ------------------------------
# ""    str         비어있는 문자열
# None  NoneType    값이 없음을 나타내는 특별한 값 

print()
print(list(range(0,0,-1)))
print(user[0:0:-1])
print(bool(range(0,0,-1)))