# fund_max3.py
print('9----------------------')
su = [5,4,7,10,6, 1]
def fmin(fu):
    min = fu[0]
    for sfu in fu:
        if min > sfu: # 5 > 4
            min = sfu
    return min

mina = fmin(su)
print(mina)