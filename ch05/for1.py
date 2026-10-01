# for1.py

# for 변수 in 리스트:
#     코드블록

# for num in [0, 1, 2]:
#     print('hi',num)
# print('for문 종료')

# print('-----------------------------------------')

characters = ['앨리스', '도도새', '3월토끼']

for character in characters:
    print(character)

print(character)
for char in character[0]:
    print(char)

print('-----------------------------------------')

nums = [0, 1, 2]
for num in nums:
    print(num)
print(nums)

print('-----------------------------------------')

nums = [0, 1, 2]
for num in nums:
    print(num)
    print(nums)

print('튜플, 딕셔너리----------------------------')
nums = (0,1,2)
for num in nums:
    print(num)

chicken = {'이름': '치킨', '나이': 1, '옷': '양념'}
for chick in chicken:
    print(chick)

print('---------------------')
for chick in chicken.items():
    print(chick,type(chick))
print('---------------------')
for chick in chicken.keys():
    print(chick,type(chick))
print('---------------------')
for chick in chicken.values():
    print(chick,type(chick)
          )

