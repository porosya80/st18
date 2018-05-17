import random

def rand_gen():
    while True:
        yield random.randint(1,1000)

def range_my(start,stop,step=1):
    while stop >= start:
        yield start
        start += step


def map_my(funct, lis):
    i = 0
    while i != len(lis):
        yield funct(lis[i])
        i += 1


def enum_my(lis):
    i = 0
    while i != len(lis):
        yield i, lis[i]
        i += 1



def x5(x):
    return x * 5

gen = map_my
gen2 = enum_my

for i in gen(x5, [1,2,3,4,5,6,7]):
    print(i)

for i in gen2([1,2,3,4,5,6,7]):
    print(i)


# for i in range_my(1, 10, 2):
#     print(f'iter # {i}')
#     print(next(rand_gen()))




