import random
def error_raise():
    err = random.randint(0,2)
    if err == 0:
        raise ValueError
    elif err == 1:
        raise TypeError
    else:
        raise RuntimeError


try:
    error_raise()
except ValueError:
    print("ValueError")
except TypeError:
    print("Type")
except RuntimeError:
    print("Run")