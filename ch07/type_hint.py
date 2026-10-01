# type_hint

# def 함수명(매개1 : 데이터타입 , 매개2 : 데이터타입) -> 반환(return)타입:
#     코드블록
#     return 반환값

# 함수명(인수1, 인수2)

def add(x : int, y : int) -> int:
    return x + y

print(add(3,5))     # 정수 입력해줘~~!
print(add(3.2,5))   # 실수 입력해도 문제 없긴 함(강제성 X)