import time


def smart_decor(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
            print("called function is:", func.__name__)
            return func(a, b)

    return inner


@smart_decor
def div(a, b):
    print("division of 2 numbers are", a / b)


@smart_decor
def mod(a, b):
    print("module of 2 numbeers are", a % b)


div(2, 4)
div(10, 4)
mod(2, 4)


# ----------------------------------------
def execution_time(originalfunction):
    def innerFunction(*args):
        start_time = time.time()
        originalfunction(*args)
        end_time = time.time()
        exec_time = start_time - end_time

        print(f'Function name is: {originalfunction.__name__} and execution time is : {exec_time}')

    return innerFunction


@execution_time
def summ(a, b):
    print("a+b is", a + b)
    return a + b


@execution_time
def sum_fun():
    result = 0
    for r in range(1, 10000):
        result = result + r
    print("Addition value is", result)
    return result


@execution_time
def mul_fun():
    result = 1
    for r in range(1, 10):
        result = result * r
    print("multiplication value is", result)
    return result


@execution_time
def mul_param(num):
    result = 1
    for r in range(0, 1000):
        result *= num
    print("multiplication value is", result)
    return result


summ(20, 33)
sum_fun()
mul_fun()
