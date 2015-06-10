import functools
from datetime import datetime
from datetime import timedelta

__author__ = 'radu.sover'

import math

def measure_execution(function):
    @functools.wraps(function)
    def inner(*args, **kwargs):
        start = datetime.now()
        result = function(*args, **kwargs)
        duration = datetime.now() - start
        print("Function {function} took {time} to execute".format(**{'function': function.__name__, 'time': duration}))
        return result  # nu merge cum ma gandeam eu
    return inner

# nu cred ca e ce se vrea.. de vazut mai tarziu
def measure_execution_totaled(function):
    internal_counter = timedelta(0,0)

    @functools.wraps(function)
    def inner(*args, **kwargs):
        nonlocal internal_counter
        start = datetime.now()
        function(*args, **kwargs)
        duration = datetime.now() - start
        internal_counter += duration
        print("Function {function} took {time} x to execute".format(**{'function': function.__name__, 'time': internal_counter}))
    return inner

def read_number():
    return int(input())


def number_prime(number):
    if special_case(number):
        return True

    if odd_number(number) is False:
        return False

    upto = math.floor(number / 2)
    step = 3

    while step < upto:
        if number % step == 0:
            return False

        step += 1

    return True


def special_case(number):
    return number == 1 | number == 2


def odd_number(number):
    return number % 2 != 0


def find_all_primes(maxnumber):
    for i in range(maxnumber):
        if number_prime(i):
            yield i


def decorator_cu_memoization():

    pass


def fibonacci(n):
    a, b = 0, 1
    # while a < n: # up to the number
    for i in range(n): # first n numbers
        yield a
        a, b = b, a+b


def fibonacci_rec(a, b, counter, length):
    if counter <= length:
        print(a)
        return fibonacci_rec(b, a+b, counter+1, length)

# valorile vor fi cachuite ca sa poata fi refolosite
def fib_pentru_memoization(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_pentru_memoization(n-1) + fib_pentru_memoization(n-2)


def memoize(f):
    memo = {}

    def wrapper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return wrapper

def map_emulator(func, iterable):
    # Write a function that emulates the map functionality:
    # it should take another function func and an iterable iterable as arguments and should return an
    # iterable of the results of applying func over each value in iterable.
    for i in iterable:
        yield func(i)


def filter_emulator(func, iterable):
    # Write a function that emulates the -filter- functionality:
    # it should take another function func and an iterable iterable as arguments
    # and should return an iterable of those values in iterable that returned a truthy value when passed to func.
    for i in iterable:
        if func(i):
            yield i


def reduce_emulator(func, iterable, initializer):
    # Write a function that emulates the -reduce- functionality:
    # it should take another function func, an iterable iterable and an initial value initializer as arguments.
    # It should return the final result of repeatedly applying func over the previous result
    # (or initializer for the first time) and the next element in iterable.
    reduced = initializer
    for i in iterable:
        reduced = func(reduced, i)

    return reduced


def bubble_sort(items):
    for i in range(len(items)):
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]


def binary_search(items, item):
    first = 0
    last = len(items) - 1
    found_position = -1

    while first <= last:
        midpoint = (first + last) // 2
        if items[midpoint] == item:
            found_position = midpoint
            return found_position
        elif items[midpoint] < item:
            first = midpoint + 1
        elif items[midpoint] > item:
            last = midpoint - 1

    return found_position

# se poate in Py2 sa fac ceva asemanator cu Py3?
def counter():
    counter.internal_counter += 1
    return counter.internal_counter


def counter_3():
    internal_counter = 0

    def increment_counter():
        nonlocal internal_counter
        internal_counter += 1
        return internal_counter

    return increment_counter


# maxcheck = read_number()

# for i in find_all_primes(maxcheck):
#     print(i)

# for i in fibonacci(maxcheck):
#    print(i)

# fibonacci_rec(0, 1, 1, maxcheck)

# for i in map_emulator(lambda d: d*d, fibonacci(maxcheck)):
#    print(i)

# for i in filter_emulator(number_prime, fibonacci(maxcheck)):
#     print(i)

# print(reduce_emulator(lambda d, dd: d+dd, fibonacci(maxcheck), 1))
# print(functools.reduce(lambda d, dd: d+dd, fibonacci(maxcheck), 1))


# 7. Use map and filter and reduce to find the sum of all numbers n lower than a given value which satisfy the following
# constraint: n * n - 1 divisible by 3 (eg. 4 * 4 - 1 == 15 and 15 div with 3).
# where should I use the map?
# print(functools.reduce(lambda n, npre: n+npre, filter(lambda n: (n * n - 1) % 3 == 0, range(maxcheck)), 0))
#
# print(reduce_emulator(lambda n, npre: n+npre,
#                       filter_emulator(lambda n: n % 3 == 0,
#                                       map_emulator(lambda n: n * n - 1,range(maxcheck))), 0))

# 8
# alist = [54,26,93,17,77,31,44,55,20]
# bubble_sort(alist)
# print(alist)
#
# print("Position of {number} is {position}".format(**{'number': 77, 'position': binary_search(alist, 77)}))


# 9
# counter.internal_counter = 0
# counter()
# counter()
# print(counter())
#
# bunny_counter = counter_3()
# bunny_counter()
# bunny_counter()
# print(bunny_counter())
#
# python_counter = counter_3()
# python_counter()
# print(python_counter())


# for i in fibonacci(maxcheck):
#     print(i)
#
# decorated_fibo = measure_execution(fibonacci_rec)
# decorated_fibo(0, 1, 1, maxcheck)
# print(decorated_fibo.__name__)

# print(fib_pentru_memoization(maxcheck))

# fib_memo = memoize(fib_pentru_memoization)
# for i in range(maxcheck):
#     print(fib_memo(i))

# for i in range(maxcheck):
#     print(fib_pentru_memoization(i))
