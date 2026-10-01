# Cexm.py

# 클래스 정의
class Cexm:
    def fsam(self):
        print('멤버함수(메서드)')
    def fsbm(self, pa):
        self.x = pa
        print('멤버 변수 x는', self.x)

# 객체 생성 => 메모리 적재
ca = Cexm()
cb = Cexm()

# 객체 접근
ca.fsam()
ca.fsbm(10)