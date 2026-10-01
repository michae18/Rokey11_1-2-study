# default1.py

# def person_a(width, height):
#     print('디폴트 매개값 없음')
#     print('width:', width, 'height:', height)

def person_b(width = 4, height = 3):
    print('디폴트 매개값 설정')
    print('width:', width, 'height:', height)

# 시도 1: 함수 오버로딩 지원 안함 -> 실패!
# def person_a():
#     print('디폴트 매개값 없음')
    # print('width:', width, 'height:', height)

# 시도 2: 기본 매개변수 활용 => 성공!
def person_a(width = 11, height = 21):
    print('디폴트 매개값 있음')
    print('width:', width, 'height:', height)

person_a(10,20)
person_a()
person_b()