# Animal.py
# 상속 / 오버라이딩 활용 프로그램 작성

## 클래스 정의 : Animal
# 객체: 고양이, 사자, 호랑이, 개, ...
# 속성: 종, 나이, 서식지, 눈, 코, 입, 무게, 길이,...
# 기능/동작: 소리내다, 자다, 먹다, 싸다, ...

class Animal:
    eye = 2
    nose = 1
    mouth = 1
    def __init__(self,name, weight, length):
        self.name = name
        self.weight = weight
        self.length = length
    def introduce(self):
        print(self.name, '종', self.weight, '무게', self.length, '길이')

    def eat(self, food):
        print(food, '먹다')
class Cat:
    def __init__(self,name, weight, length,claude):
            self.name = name
            self.weight = weight
            self.length = length
            self.claude = claude
    def introduce(self):        # 자식 메서드 재정의
        print(self.name, '종', self.weight, '무게(kg)', self.length, '길이(m)', self.claude, '무리 여부(T/F)')
    
    def eat(self, food):        # 자식 메서드 재정의
        print(food, '먹다')

    def Sound(self,sound):      # 자식 메서드
         print('울음소리',sound)

class Tiger:
    def __init__(self,name, weight, length,claude):
            self.name = name
            self.weight = weight
            self.length = length
            self.claude = claude
    def introduce(self):
        print(self.name, '종', self.weight, '무게(kg)', self.length, '길이(m)', self.claude, '무리 여부(T/F)')
    
    def eat(self, food):
        print(food, '먹다')

    def Sound(self,sound):
             print('울음소리',sound)



tiger = Tiger('호랑이', 120, 2.3, False)
tiger.introduce()
tiger.Sound('어흥')
tiger.eat('토끼')

print('\n-------------------------')
cat = Cat('나비', 3.5, 0.2, True)
cat.introduce()
cat.Sound('야옹')
cat.eat('츄르')