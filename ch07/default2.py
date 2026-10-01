# default1.py

# 기본 매개 변수 없이 사용
def person_c(height, width, age):
    print('디폴트 매개값 설정')
    print('키:', height, '몸무게:', width, '나이:', age)
person_c(168,55,23)
print('-------------------------------------------------')

# 기본 매개 변수 없이 사용
def person_c(height, weight, age):
    print('디폴트 매개값 설정')
    print('키:', height, '몸무게:', weight, '나이:', age)
person_c(168,55,26)

# 기본 매개 변수 일부 사용 : 뒤에서부터 설정할 것!
# def person_c(height, weight=50, age):
#     print('디폴트 매개값 설정')
#     print('키:', height, '몸무게:', weight, '나이:', age)
# person_c(168,26)

# 1. 모든 매개변수에 기본값 설정 가능
# 2. 기본값이 있더라도 인수 설정 가능(인수 우선 처리)
# 3. 부분 매개변수에 기본값 설정 시, 뒤에서부터 설정할 것.
# 4. 인수 전달 시 앞에서부터 설정할 것.

# 위치 인수: 순서대로 전달하는 인수
person_c(174,77)
# 키워드 인수: (매개변수) 이름을 지정해서 전달하는 인수
person_c(weight = 55)

range()

# 위치 + 키워드 인수
person_c(178, age = 28)

활용예시
print('hi','hello',end='', sep='/')