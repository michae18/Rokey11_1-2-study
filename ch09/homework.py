# homework.py

# 3. 내부 코드가 없는 핸드폰 클래스 정의
# class Phone:
#     pass

# # 4. 핸드폰 클래스의 인스턴스 생성하고, 이를 my_phone 변수로 할당해보세요.
# class Phone:
#     pass

# my_phone = Phone()

# # 5. 핸드폰 (Phone) 클래스에 "휴대폰 생성"를 출력하는 생성자를 추가하세요.
# class Phone:
#     def __init__(self,maker,make_year,color):
#         pass

# my_phone = Phone()

# 6. 핸드폰 (Phone) 클래스에 (제조사, 출고년도, 색상)을 입력받는 생성자를 추가하세요
class Phone:
    def __init__(self,maker,make_year,color):
        self.maker = maker
        self.make_year = make_year
        self.color = color

my_phone = Phone('삼성',2019,'black')
print(my_phone.maker)
print(my_phone.make_year)
print(my_phone.color)

# 7. 앞서 생성한 인스턴스의 제조사, 출고년도, 색상을 출력하시오.
# #  인스턴스 변수에 접근하여 값을 출력 합니다.
class Phone:
    def __init__(self,maker,make_year,color):
        self.maker = maker
        self.make_year = make_year
        self.color = color

my_phone = Phone('삼성',2019,'black')
print(my_phone.maker)
print(my_phone.make_year)
print(my_phone.color)

# 8. 핸드폰 (Phone) 클래스에서 제조사, 출고년도, 색상을 출력하는 info() 메소드를 추가하세요.
class Phone:
    def __init__(self,maker,make_year,color):
        self.maker = maker
        self.make_year = make_year
        self.color = color
    def info(self):
        print('제조사',self.maker, 
              '제조년도', self.make_year, '색상:', self.color)

my_phone = Phone('삼성',2019,'black')
print(my_phone.maker)
print(my_phone.make_year)
print(my_phone.color)


# 9. 핸드폰 (Phone) 클래스에 (제조사, 출고년도, 색상)을 매개변수로 사용하여 기 생성된 맴버 변수를 수정하는 setInfo 메소드를 추가하세요.
class Phone:
    def __init__(self,maker,make_year,color):
        self.maker = maker
        self.make_year = make_year
        self.color = color
    def info(self):
        print('제조사',self.maker, 
              '제조년도', self.make_year, '색상:', self.color)
    def setinfo(self, maker,make_year,color):
        self.maker = maker
        self.make_year = make_year
        self.color = color


my_phone = Phone('삼성',2019,'black')
print(my_phone.maker)
print(my_phone.make_year)
print(my_phone.color)
my_phone.info()
my_phone.setinfo('LG', 2020, 'white')
my_phone.info()