# 7.1
# x = 10

# def example1():
#     x = 20
#     print(x)

# example1()
# print(x)

# # 7.2
# x = 5

# def example2():
#     global x
#     x = 15
#     print(x)

# example2()
# print

# 8.1
# 리스트에서 최대값을 찾아 출력하는 아래 함수의 빈 칸 a, b에 알맞은 코드를 작성하시오.
# def list_max(num_list):
# max = num_list[0]
# 		for num in num_list:
# 			if <    a    >:
# 			   <    b    >
# 		print(max)
# def list_max(num_list):
#     max = num_list[0]
#     for num in num_list:
#         if num > max :
#             max = num
#     print(max)
# numbers = [10, 1, 5, 15, 7]
# list_max(numbers)

# 8.2 주어진 리스트에서 최솟값을 찾는 프로그램을 작성하시오.
numbers = [42, 17, 23, 56, 9, 34]

def find_min(nums):
    min_num = nums[0]
    for num in nums:
        if min_num > num:
            min_num = num
    print(min_num)

find_min(numbers)
