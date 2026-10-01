# list.insert.py

# 특정 위치에 값 추가하기
# 리스트변수명.insert()

clovers = ['클로버1', '클로버2', '클로버3']
clovers.insert(0,'클로버0')
print(clovers)

clovers.insert(1, '하트1')
print(clovers)

print('---------------------------------------')
# 여러 값 추가하기
clovers.extend(['하트2','클로버4'])
#리스트로 만들어서 추가해도 됨.
new_list = ['하트3','스페이드1']
clovers.extend(new_list)
print(clovers)