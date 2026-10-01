# tuple1.py

# tuple 생성 방법
# 튜플 변수명 = (요소1, 요소2, 요소3)

'''
리스트 : 데이터 값 변경 가능(추가, 수정, 삭제 가능)
튜플 : 데이터 값 변경 불가(추가, 수정, 삭제 불가)
'''

clovers = ('클로버1', '하트2', '클로버3')
print(type(clovers))
print(clovers[1])

print('------------------------------------')
my_tuple = ()
print(my_tuple)
print(type(my_tuple))

print('------------------------------------')
# 변수명 = (요소1,) 요소 1개 있는 튜플은 뒤에 , 추가하기
clovers = ('클로버1',)
clover_ = '클로버1',
clover_Str = ('클로버1')
print(clovers)
print(type(clovers)) # 튜플
print(type(clover_Str)) # str
print(type(clover_))
clovers = ['클로버1'] # list는 단독으로 사용 가능
print(clovers)
print(type(clovers)) # list


a= (1,2,3)
print(type(a))
a= list((1,2,3))
print(type(a), a)
new_a = list(a) # 튜플을 리스트로 변경하는 법
new_a[0] = 7
print(new_a)

new_new_a = tuple(new_a) #리스트를 튜플로 변경하는 법
print(new_new_a , type(new_new_a))
