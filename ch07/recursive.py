# recursive.py

# 재귀함수
# def 함수명(매개변수):
#     코드블록
#     함수명(인수)
#     return 반환값

def count_down(n):
    if n == 0:
        print('새해가 밝았습니다')
        return
    print(n)
    count_down(n-1)

count_down(5)

# [문제] 수학의 팩토리얼(!)을 구하시오!
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    
print(factorial(5))

# 5 * factorial(4)
# 5 * 4 * factorial(3)
# 5 * 4 * 3 * factorial(2)
# 5 * 4 * 3 * 2 * factorial(1)

# 실무 활용 예시
# 폴더 탐색, 알고리즘(트리구조)