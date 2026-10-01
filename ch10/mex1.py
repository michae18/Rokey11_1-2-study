# mex1.py
print('mex1.py')
print(__name__)

# 클래스
class Cvalue():
    def __init__(self):
        self.lista = []
    def add(self,num):
        self.lista.append(num)
    def fprint(self):
        print(self.lista)

#함수
def plus(a,b):
    c = a + b
    return c

# 변수
p1 = Cvalue()
# print(p1.lista)
p1.add(1)
p1.add(2)
p1.add(3)
p1.fprint()
print(plus(5,6))