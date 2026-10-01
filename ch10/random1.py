# random1.py

import random

animals = ['체셔고양이','호랑이','오리','도도새','고래']
print(random.choice(animals))
print(random.choice(animals))
print(random.choice(animals))

print('--------------------------')
flowers = ['장미','들꽃','민들래','백합','국화','수선화']
print(random.sample(flowers,2))
print(random.sample(flowers,3))



print('--------------------------')
ran_num = random.randint(1,42)
if ran_num > 3 :
    print('당청되었습니다')