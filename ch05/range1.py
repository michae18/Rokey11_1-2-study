# range1.py

# range(인수)
# range(시작 정수, 끝 정수)
# range(인수1, 인수2, 인수3)


print(range(10)) # range(0,10)
print(type(range(10)))
print(list(range(10)))

print(range(3,10))
print(list(range(3,10)))

print(range(8,14,2))
print(list(range(8,14,2)))

print('--------------------')
for num in range(3):
    print(num)