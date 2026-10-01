# Student.py

## 클래스 정의 : Human
# 객체: 사람1, 사람2, 사람3, ...
# 속성: 이름, 나이, 직업, 눈, 코, 입, ...
# 기능/동작: 자기소개하다, 자다, 먹다, 말하다, ...


class Human:
    eye = 2
    nose = 1
    mouth = 1
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(self.name, self.age)
    def eat(self, food):
        print(food, '먹다')
    def sleep(self):
        print('자다')
    def talk(self):
        print('말하다')

print('눈 개수',Human.eye)
lee = Human('이수근', 49)
lee.introduce()
lee.eat('치킨')
print(lee.name)

print('------------------------')
## 클래스 정의: student
# 객체: lee, kim, park, choi
# 속성: 이름, 나이, 직업, 눈, 코, 입, 학번, ...
# 기능/동작: 자기소개하다, 자다, 먹다, 말하다, 공부하다, ...
class Student(Human):
    def __init__(self, name, age, student_num):
        self.name = name
        self.age = age
        self.student_num = student_num
    def study(self):
        print('공부하다')

kim = Student('김수로', 17, 202023078)
print(kim.student_num)  # 자식 속성
kim.introduce()         # 부모 메서드 상속
kim.sleep()             # 부모 메서드 상속
kim.study()             # 자식 메서드

