# priority.py

'''
연산자 우선순위
괄호 > 산술 연산자 > 비교 연산자 > 논리 연산자 > 대입
산술: ** > +x , -x > *, /,, //, % > + , -
논리: not > and > or
비교: 같은 우선 순위
'''
print(2 * (3 - 5))

print('-----------------------------')

print(9 > 4 and 3 > 2)  # T and T => True
print(9 < 4 and 3 > 2)  # F and T => False
print(9 < 4 or 3 < 2)   # F or F => False
print(9<4 or 3>2)       # F or T => True

print('-----------------------------')

print((3 - 5) < 1)              # -2 < 1 => T
print(3 - 5 < 1)                # -2 < 1 => T
print(3 - 5 < 1 and 3 - 5 > 1)  # (-2 < 1) and -2 > 1 = T and F => F