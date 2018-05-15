import random

sp = [random.randint(1, 100) for _ in range(random.randint(1, 100))]


ind  = input("index,please: ")

try:
    print(sp[int(ind)])
except ValueError:
    print('use digits')
except IndexError:
    print('index not in range')
finally:
    print('That`s all guys')
