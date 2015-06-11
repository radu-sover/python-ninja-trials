__author__ = 'radu.sover'

import functions
import re

class Stream:
    def write(self, s):
        print(s)


# 2. Write all the prime numbers lower than a given number in a file, one number per line.
# aici am pus ca si parametru un obiect ce ar avea functia write implementata...
# cat de des se intampla in Py ceva de genul
def write_prime_numbers(prime_numbers, writer):
    '''
    :param prime_numbers: iterable of prime numbers
    :param writer: the place to put those numbers
    :return: pass
    >>> write_prime_numbers([1,3,5,7,11], writer=Stream())
    1
    <BLANKLINE>
    3
    <BLANKLINE>
    5
    <BLANKLINE>
    7
    <BLANKLINE>
    11
    <BLANKLINE>
    '''
    for i in prime_numbers:
        writer.write('%s\n'%str(i))

    pass


# 1. Compute the sum of all the numbers in a file. The file contains a number on each line.
def compute_sum(file_name):
    '''
    not a real doctest - the file read could be mocked
    >>> compute_sum('prime_numbers_file')
    196
    '''
    sum = 0
    with open(file_name, 'r') as f:
        for line in f:
            sum += int(line)


    return sum


# 3. Find all the words used only once in a file containing text.
def find_unique_words(file):
    split_pattern = '; |, |\*|\n |_ |\s'
    search_pattern = '\W+'
    one_occurrence = []
    multi_occurrence = []

    for line in f:
        # for word in line.encode(encoding='utf-8').split(): # Daca fisierul e deschis cu encoding implicit
        # for word in re.split(split_pattern, line):
        for word in map(lambda x: str.lower(x), re.split(search_pattern, line)):
            # unique_hash = hash(word)
            if (word not in multi_occurrence) and (word not in one_occurrence):
                one_occurrence.append(word)
            elif word in one_occurrence:
                one_occurrence.remove(word)
                if word not in multi_occurrence:
                    multi_occurrence.append(word)

    return one_occurrence, multi_occurrence

# 4. Write a program that reads a number of files containing sorted numbers (one number per line)
# and outputs a large file with all the numbers from all the files sorted.


# 5. Extract all the links in a website on a given URL.



if __name__ == '__main__':
    # problema 2 imi genereaza content pt problema 1
    primes = functions.find_all_primes(40)
    with open('prime_numbers_file', 'w') as f:
        write_prime_numbers(primes, f)

    # problema 1 foloseste content
    print(compute_sum('prime_numbers_file'))

    # problema 3: numaratoare
    with open('text.txt', 'r', encoding='latin-1') as f:
        single, multiple = find_unique_words(f)
        print("Single: ", single[:10], ' ... first 10')
        print("Multiple: ", multiple[:10], ' ... first 10')

    print('nothing else here')