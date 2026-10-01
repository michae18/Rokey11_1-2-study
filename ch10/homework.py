# 5. 다음 코드가 동작하도록 핸드폰 (Phone) 클래스를 정의하세요.
# phone = Phone("010-1234-5678", "검정")
# print(phone.number)
# print(phone.color) 
# 실행결과: 
# 010-1234-5678
# 검정

class Phone:
    def __init__(self,number, color):
        self.number = number
        self.color = color

phone = Phone('010-1234-5678', '검정')
print(phone.number)
print(phone.color) 

# 6. 핸드폰 (Phone) 클래스를 상속받은 스마트 폰 (SmartPhone) 클래스를 정의하세요.

class Phone:
    def __init__(self,number, color):
        self.number = number
        self.color = color

phone = Phone('010-1234-5678', '검정')
print(phone.number)
print(phone.color) 

class SmartPhone(Phone):
    def __init__(self, number, color):
        super().__init__(number, color)


# 7. 다음 코드가 동작하도록 스마트 폰 (SmartPhone) 클래스를 정의하세요. 단, 스마트 폰 클래스는 핸드폰 클래스를 상속받습니다.
# apple = SmartPhone("010-1234-5678", "검정", "애플")
# print(apple.number)
# print(apple.color)
# print(apple.company)
# 실행결과:
# 010-1234-5678
# 검정
# 애플
print('----------------------------------------')

class Phone:
    def __init__(self,number, color):
        self.number = number
        self.color = color 
    

class SmartPhone(Phone):
    def __init__(self, number, color, company):
        super().__init__(number, color)
        self.company = company

apple = SmartPhone("010-1234-5678", "검정", "애플")
print(apple.number)
print(apple.color)
print(apple.company)

print('---------------------------')
# 8. 다음 코드가 동작하도록 핸드폰 (Phone) 클래스를 수정하세요.
# phone = Phone("010-1234-5678", "검정")
# phone.showInfo()
# 실행결과:
# 전화번호: 010-1234-5678
# 색상: 검정

class Phone:
    def __init__(self,number, color):
        self.number = number
        self.color = color 
    def showInfo(self):
            print('전화번호:',self.number)
            print('색상:',self.color)

phone = Phone("010-1234-5678", "검정")
phone.showInfo()

print('----------------------------------')
# 10. 다음 코드가 동작하도록 스마트 폰 (SmartPhone) 클래스를 수정하세요. 
# apple = SmartPhone("010-1234-5678", "검정", "애플")
# apple.showInfo()

class SmartPhone(Phone):
    def __init__(self, number, color, company):
        super().__init__(number, color)
        self.company = company
    def showInfo(self):
        super().showInfo()
        print('회사:', self.company)

apple = SmartPhone("010-1234-5678", "검정", "애플")
apple.showInfo()