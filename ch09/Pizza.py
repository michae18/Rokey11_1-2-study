# Pizza.py

# class 클래스명:
    # pass
    # 1. 함수
    # def 함수명(self, 매개1, 매개2):
    #     코드블록
    #     self.변수명 = 데이터 값
    #     return 반환값
    # 2. 변수
    # 변수명 = 데이터값

class Pizzaclass:
    # 1. 함수
    def order(self):
        print('주문하다.')
        self.kind = 10  # 종류 10개

    # 2. 변수
    large = 21          # 변수 

# 객체 생성
# 객체변수명 = 클래스명() # 생성자 함수
pizza1 = Pizzaclass()

# 객체변수명.함수명(인수)
# 객체변수명.변수명
pizza1.order()  # 함수 호출
print(pizza1.large)    # 변수 접근        
print(pizza1.kind)