# Bag.py

## 클래스에 정의: 가방
# 객체 : 에코백, 핸드백, 백팩, ...
# 속성 : 제조사, 색상, 가격, 재질, ...
# 동작/기능(메서드) : 넣다, 열다, 매다, 지퍼를 닫다, ...

class Bag:
    # 1. 멤버변수(속성, 명사)
    call_name = 'self'
    data = []       # 클래스 멤버변수 => 설계도 공유 데이터(공통 메모리)
    # 스패셜 메서드: 
    # 클래스 초기화 시 필요한 데이터 및 기능 추가 가능
    # 각 객체의 메모리 공간에 추가
    def __init__(self, name):
        self.data= []
        print(name)

    # 2. 메서드(기능/동작, 동사)
    def add(self, x):
        print(x,'넣다')
        self.data.append(x)
        print(self.data)

    def open(self):
        print('열다')

    def close(self):
        print('닫다')

    def remove(self,x):
        print(x,'꺼내다')
        self.data.remove(x)
        print(self.data)

    def add_twice(self,x):
        print(x,'두번 넣기')
        self.data.append(x)
        self.data.append(x)
        print(self.data)

eco_bag = Bag('에코백')
# print(eco_bag.call_name)
print(Bag.call_name)
eco_bag.open()
eco_bag.add('생수')
eco_bag.add('과자')
eco_bag.remove('생수')
eco_bag.close()

print('------------------')
handbag = Bag('핸드백')
print(handbag.call_name)
handbag.open()
handbag.add('핸드폰')
handbag.add('이어폰')
handbag.remove('핸드폰')
# 실습: 새 가방 객체를 선언하고, 물건 담아보기(두번 담기 기능 추가)
print('------------------')
backpack = Bag('배낭')
backpack.add('에어팟')
backpack.add_twice('휴대폰')
backpack.add('지갑')
backpack.remove('에어팟')
backpack.add('노트북')


# Mutable(뮤터블) - 변경 가능 객체 예) list, dict, set
#  : 객체 생성 후, 내용 변경 가능
# Immutable(이뮤터블) - 변경 불가능 객체, 예) int, float, bool, str, tuple
#  : 객체 생성 후, 내용 변경 불가능