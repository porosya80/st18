import time

count = [0, ]

def deny_f(func):
    def inner(text):
        print(f'This {func.__name__} is canceled')
        # func(text)
    return inner


def time_calc(func):
    def inner(n):
        start = time.time()
        func(n)
        stop = time.time()
        print(f'{func.__name__} done in {stop - start} seconds')
    return inner

def counter(func):
    def inner(text):
        count[0] += 1
        func(text)
        print(count[0])
    return inner


def loggi(func):
    print(f'Create a decorator for {func.__name__}')

    def inner(text):
        print('start function')
        func(text)
        print('end function')
    return inner


def try_ex(func):
    def inner(text):
        try:
            func(text)
        except ZeroDivisionError as e:
            print(e)
    return inner





@try_ex
def err(text):
    return 4 / 0

@time_calc
def sleep(n):
    print('hrrrrr')
    time.sleep(n)
    print('Wake Up')



@deny_f
def say_hi(name):
    print(f'Hello to {name}')



@counter
def hi(text):
    print(text)


@loggi
def bye(text):
    print(text)



def main():
    say_hi("vasya")
    sleep(0)
    bye('bddd')
    for i in range(5):
        hi("ppp")
    err("some")

if __name__ == '__main__':
    main()