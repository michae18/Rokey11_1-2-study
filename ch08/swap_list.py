# swap_list.py
# ca = [10,11]
# print('ca[0]의 값은', ca[0], 'ca[1]의 값은', ca[1])
# temp = ca[0]
# ca[0] = ca[1]
# ca[1] = temp
# print('ca[0]의 값은', ca[0], 'ca[1]의 값은', ca[1])

print('------------------------------')

# def funca(na, nb):
#     temp = na
#     na =nb
#     nb = temp
    
# # ca=[10,11]
# # na =ca[0]
# # nb = ca[1]

# print('ca[0]의 값은', ca[0], 'ca[1]의 값은', ca[1])
# funca(ca[0],ca[1])
# print('ca[0]의 값은', ca[0], 'ca[1]의 값은', ca[1])

print('-------------------------------')
# ca = [10,11]
# cb = ca
# print('리스트 ca:', ca)
# print('리스트 cb:', cb)
# print('리스트 ca 주소:', id(ca))
# print('리스트 ca[0] 주소:', id(ca[0]))
# print('리스트 ca[1] 주소:', id(ca[1]))
# print('리스트 cb 주소:', id(cb))
# print('리스트 cb[0] 주소:', id(cb[0]))
# print('리스트 cb[1] 주소:', id(cb[1]))

print('-------------------------------')
# ca = [10,11]
# cb = ca
# print('리스트 ca:', ca)
# print('리스트 cb:', cb)
# temp = ca[0]
# ca[0] = ca[1]
# ca[1] = temp
# print('리스트 ca:', ca)
# print('리스트 cb:', cb)
# print('ca[0]:', ca[0], 'ca[1]:', ca[1])
# print('cb[0]:', cb[0], 'cb[1]:', cb[1])

# print('리스트 ca 주소:', id(ca))
# print('리스트 ca[0] 주소:', id(ca[0]))
# print('리스트 ca[1] 주소:', id(ca[1]))
# print('리스트 cb 주소:', id(cb))
# print('리스트 cb[0] 주소:', id(cb[0]))
# print('리스트 cb[1] 주소:', id(cb[1]))
ca = [10,11]
print('리스트 ca:', ca)
def funca(cb):
    temp = ca[0]
    ca[0] = ca[1]
    ca[1] = temp
ca = [10,11]    # cb = ca

print('ca[0]:', ca[0], 'ca[1]:', ca[1])
funca(ca)
print('ca[0]:', ca[0], 'ca[1]:', ca[1])

print('리스트 ca 주소:', id(ca))
print('리스트 ca[0] 주소:', id(ca[0]))
print('리스트 ca[1] 주소:', id(ca[1]))

print('-------------------------------')

# def funcb(pa, pb):
#     temp = pa
#     pa = pb
#     pb = temp
#     return pa, pb

# ca = [10]
# cb = [11]


# print('ca:', ca, 'cb:', cb)
# ca, cb = funcb(ca, cb)
# print('ca:', ca, 'cb:', cb)