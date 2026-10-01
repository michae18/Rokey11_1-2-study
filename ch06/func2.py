# func2.py

# 함수 정의
def funca(pa,pb):
    nc = pa + pb
    return nc

na = 10
nb =11

# 함수 호출
# funca(na,nb)  # funca(10,11)
nd = funca(na,nb)   # funca(10,11)
# pa =na
# pb = nb

# print(na, '+', nb, '=', nc)
print(na, '+', nb, '=', nd)

print('--------------------------')
def fplusminus(arg):
    if arg > 0:
        return 'plus'
    elif arg < 0:
        return 'minus'

stra = fplusminus(1)
print(stra)
print(stra[0])
print(stra[1])

print('---------------------------')
def myabs(arg):
    if arg < 0:
        result = arg * -1
    else:
        result = arg
    return result

print(myabs(-3))



