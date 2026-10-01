# dict1.py

# 딕셔너리
# 리스트: [item1, item2, item3, ...]
# 딕셔너리: {key1:val1, key2:val2, key3:val3, ...}

# 빈 딕셔너리
my_dict1 = {}

my_dict2 = {0:1, 1:-2, 2:3.14}
print(my_dict2, type(my_dict2))

my_dict3 = {'이름':'앨리스', '나이':10, '시력':[1.0,1.2]}
# 같은 키 이름 사용 시 재할당 되어 덮어씌워짐.
my_dict3 = {'이름':'앨리스', '나이':10, '시력':[1.0,1.2], '이름': '정민혁'}
print(my_dict3, type(my_dict3))

print('--------------------------------------------------')
# 딕셔너리 데이터 추가 방법
# 딕셔너리 변수명['키'] = 데이터 값
my_dict3['성별'] = '여성'
print(my_dict3, type(my_dict3))
my_dict3['직업'] = '개발자'
print(my_dict3, type(my_dict3))

print('--------------------------------------------------')

#각자의 데이터를 활용하여 딕셔너리를 생성하고, 
# 추가하고 값에 접근해보세요

my_data = {'이름': '정민혁','나이': 26, '키' : 177}
print(my_data)
my_data['직업'] = ['백수', '개발자']
print(my_data)
my_data['번호'] = '010-1234-5678'
print(my_data)
print(my_data.get('이메일')) # 없는 키 호출 시 none 출력 
# 없는 키 호출 시 none 대신 '주소 없음' 출력
print(my_data.get('주소','주소 없음'))

print('--------------------------------------------')

print(my_dict3.items(), type(my_dict3.items()))

print(my_dict3.keys())
print(my_dict3.values())