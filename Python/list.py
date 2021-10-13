import random

def pri(this):
    for r in range(10):
        print(this[0:10])
        this = this[10:]


lis = []
i = 0

while i<100:
    a = random.random()
    lis.append(round(a, 4))
    i += 1

pri(lis)
print('Вторая прогонка')
lis.sort()
pri(lis)
