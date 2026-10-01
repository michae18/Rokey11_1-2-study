# slicing.py

# 슬라이싱
# 리스트명[start:stop]

week=['월','화','수','목','금','토','일']
print(week[2])
print(week[3:7])
print(week[1:5])

print('-----------------------------------------')
# 인덱스 생략 가능
# 1. 시작 인덱스가 0인 경우
print(week[:3])
# 2. 마지막 데이터까지 접근하는 경우
print(week[1:])
# 3. 전체 데이터 접근하는 경우
print(week[:])

# 리스트명[start:stop:step]
# start: 시작 인덱스
# stop: 끝 인덱스(미포함)

week=['월','화','수','목','금','토','일']
print(week[1:5])
print(week[1:5:1])
print(week[1:5:2])
# print(week[1:5:0]) # step에 0을 넣을 수 없다

print('음수 인덱싱-------------------------------')
# 인덱스 번호 음수 가능: 뒤에서부터 접근
print(week[-1])
print(week[-2])
print(week[-3])

print('음수 슬라이싱-------------------------------')
print(week[-3:-1])
print(week[-5:5])
print(week)
# 슬라이싱 하였을 때 중간에 띄워져 있으면 출력이 안된다~!
print(week[-3:3])
print(week[6:5])
