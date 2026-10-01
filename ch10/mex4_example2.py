# mex1_example2.py

# print('mex3.py')
#  from 모듈명 import 함수명
print(__name__)
from mex4 import Cvalue
from mex4 import plus

print(plus(11,22))

p3 = Cvalue()

p3.add(11)
p3.add(22)
p3.add(33)
p3.fprint()
