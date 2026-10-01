# list_remove.py

# 값을 제거하기
# 리스트명.remove(제거할 값)


subject = ['국어', '수학', '영어', '국사']
# subject.remove('영어')
print(subject[2])
print(subject[1:3])
subject.remove(subject[1])
print(subject)
subject.append('영어')
print(subject)

print('--------------------------------------')

''' 
del과 remove의 차이점:
del : index를 사용하여 제거
insert: 데이터 명을 사용하여 제거
'''

clovers = ['클로버1', '클로버2', '클로버3']
print(clovers[1])

del clovers[1]
print(clovers)
print(clovers[1])