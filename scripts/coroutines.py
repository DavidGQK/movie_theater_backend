# import math

# def cash_return(deposit: int, percent: float, years: int) -> float:
#     value = math.pow(1 + percent / 100, years)
#     return round(deposit * value, 2) 

# print(cash_return(1_000_000, 5, 5))



# import math


# def cash_return_coro(percent: float, years: int) -> float:
#     value = math.pow(1 + percent / 100, years)
#     while True:
#         try:
#             deposit = (yield)
#             yield round(deposit * value, 2)
#         except GeneratorExit:
#             print('Выход из корутины')


# coro = cash_return_coro(5, 5)
# next(coro)
# values = [1000, 2000, 5000, 10000, 100000]
# for item in values:
#     print(coro.send(item))
#     next(coro)
# coro.close()


# import random
# from time import sleep


# def generate_numbers(target):
#     while True:
#         value = random.randint(1, 11)
#         target.send(value)
#         sleep(0.1)

# def double_odd(target):
#     while True:
#         value = (yield)
#         if value % 2 != 0:
#             value = value ** 2
#         target.send(value)

# def halve_even(target):
#     while True:
#         value = (yield)
#         if value % 2 == 0:
#             value = value // 2
#             target.send(value)

# def print_sum():
#     buf = []
#     while True:
#         value = (yield)
#         buf.append(value)
#         if len(buf) == 10:
#             print(sum(buf))
#             buf.clear()


# printer_sink = print_sum()
# printer_sink.send(None)
# even_filter = halve_even(printer_sink)
# even_filter.send(None)
# odd_filter = double_odd(even_filter)
# odd_filter.send(None)
# generate_numbers(odd_filter)


from functools import wraps
def coroutine(func):
    @wraps(func)
    def inner(*args, **kwargs):
        fn = func(*args, **kwargs)
        next(fn)
        return fn
    return inner

import random
from time import sleep


@coroutine
def generate_numbers(target):
    while True:
        value = random.randint(1, 11)
        target.send(value)
        sleep(0.1)

@coroutine
def double_odd(target):
    while True:
        value = (yield)
        if value % 2 != 0:
            value = value ** 2
        target.send(value)

@coroutine
def halve_even(target):
    while True:
        value = (yield)
        if value % 2 == 0:
            value = value // 2
            target.send(value)

@coroutine
def print_sum():
    buf = []
    while True:
        value = (yield)
        buf.append(value)
        if len(buf) == 10:
            print(sum(buf))
            buf.clear()


printer_sink = print_sum()
even_filter = halve_even(printer_sink)
odd_filter = double_odd(even_filter)
generate_numbers(odd_filter)