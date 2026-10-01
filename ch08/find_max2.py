su = [5,4,7,10,6]

def fmax(a,b,c,d,e):
    fu = []
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
    return max

max = fmax(su[0],su[1],su[2],su[3],su[4])
print('최대값 max는', max)

print('5----------------------')
def fmax(a,b,c,d,e):
    fu = []
    fu.append(a)
    fu.append(b)
    fu.append(c)
    fu.append(d)
    fu.append(e)
    max = fu[0]
    for sfu in fu:
        if max < sfu:
            max = sfu
        return max
max = fmax(su[0], su[1], su[2], su[3], su[4])
print('최대값 max:', max)

print('7----------------------')
su = [5,4,7,10,6]
def fmax(fu):
    max = fu[0]
    for i in range(1,5,1):
        if max < fu[i]:
            max = fu[i]
        return max
max = fmax(su)


