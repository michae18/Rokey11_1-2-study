# homework_08.py
# 1. 다음 코드의 실행 결과로 올바른 것은?
# a = [1, 2, 3, 4]
# a[0], a[3] = a[3], a[0]
# print(a)

# 3. 리스트 arr = [3, 6, 9, 12]가 주어졌을 때, 첫 번째와 세 번째 요소를
#  스왑한 결과를 출력하는 코드를 작성하세요.
# arr = [3, 6, 9, 12]
# temp = arr[1]
# arr[1] = arr[3]
# arr[3] = temp
# print(arr)

# 4
# a = [1,2,3]
# b = a
# print('a_id:',id(a), 'b_id:',id(b))

# # 5
# x = 42
# y = 42.0
# print(id(x) == id(y))

# 6. 리스트에서 첫 번째 짝수와 마지막 홀수를 찾아 서로 스왑하는 프로그램을 작성하시오

# def swap_first_Even_last_Odd(numbers_list):
#     count_Even = 0
#     for number in numbers_list:
#         if number % 2 == 0:
#             count_Even += 1
#             if count_Even == 1:
#                 first_Even = number
#         else :
#             Odd = number
#     temp = first_Even
#     first_Even = Odd
#     Odd = temp
#     return first_Even , Odd

# a = [3, 6, 7, 4, 9, 10, 13]
# print(swap_first_Even_last_Odd(a))

# 7. 파이썬으로 최대값을 찾는 알고리즘을 구현하시오.
# def find_max_num(numbers):
#     max = numbers[0]
#     for num in numbers:
#         if num > max:
#             max = num
#     return max

# a = [1,2,3,8,6,10,7]
# print(find_max_num(a))

# 8. 주어진 리스트 [29, 10, 14, 37, 13]을 선택 정렬로 한 단계 수행한 결과는 무엇인가요?
data = [29, 10, 14, 37, 13]
# 첫 번째 단계: 최소값을 찾아 첫 번째 값과 교환
# min_num = data[0]
# for num in data:
#     if num < min_num:
#         min_num = num
#         temp = data[0]
#         data[0] = min_num
#         min_num = data[0]
# print(data)


# 10. 주어진 딕셔너리에서 모든 값의 합을 구하는 함수를 작성하세요.
def add_nums(numbers):
    total = 0
    for num in numbers.values():
        total += num
    return total

dict = {'a': 10, 'b': 20, 'c': 30}

dict.values
print(add_nums(dict))
