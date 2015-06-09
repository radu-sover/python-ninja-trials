__author__ = 'radu.sover'
import math
import time

def test_prompt(prompt):
    return "for test"

def test_1(input_wrap=input):
    """
    >>> test_1(input_wrap=lambda x:"Radu")
    'UDAR'
    >>> test_1(input_wrap=test_prompt)
    'TSET ROF'
    """
    name = input_wrap("Enter your name")
    return name.upper()[::-1]


def test_2(number):
    """
    Check for a number to be a palindrom
    >>> test_2(2)
    True
    >>> test_2(13131)
    True
    >>> test_2(13334)
    False
    """

    temp_number, reversed_number = number, 0

    while temp_number > 0:
        last_digit = temp_number % 10
        reversed_number = reversed_number * 10 + last_digit
        temp_number //= 10

    return number == reversed_number

def test_3(search_up_to_number):
    """
    >>> list(test_3(12))
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
    """
    return (x for x in range(search_up_to_number) if test_2(x))


def print_palindrom(number):
    este = 'este' if test_2(number) else 'nu este'
    print('Numarul introdus {number} {este} palindrom'.format(number=number, este=este))

if __name__ == '__main__':
    print(test_1())

    for i in test_3(65487):
        print(i)

    print_palindrom(1155665511)