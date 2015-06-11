__author__ = 'radu.sover'

import re

import functions


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
def minimum_item(position_values):
    position = 0
    minimum = None
    for x in position_values:
        if minimum is None or minimum > position_values[x]:
            minimum = position_values[x]
            position = x
    return position, minimum


def sort_files(file_streams, output_stream):
    '''Quick implementation
    :param file_streams: iterable of stream with ordered items
    :param output_stream: stream where the results will be written in ordered sequence
    :return: pass
    '''
    new_line = '\n'
    position_values = {x: int(files_streams[x].readline().rstrip(new_line)) for x in range(len(files_streams))}

    while len(position_values) > 0:
        position, minimum = minimum_item(position_values)
        output_stream.write(str(minimum) + new_line)
        read = files_streams[position].readline()
        if read == '':
            del position_values[position]
        else:
            position_values[position] = int(read.rstrip(new_line))
    pass

# 5. Extract all the links in a website on a given URL.
# can I use memoize? ... ceva paralelizare...
# am observat ceva ciudat aici, in links am avut cand main primul, cand era al doilea..
def crawl_website_links(url):
    links = {}

    def crawl(url):
        links[url] = "crawled"
        pass

    links[url] = "MAIN"
    crawl("second")

    return links


if __name__ == '__main__':
    # problema 2 imi genereaza content pt problema 1
    primes = functions.find_all_primes(40)
    with open('prime_numbers_file', 'w') as f:
        write_prime_numbers(primes, f)
        print('1. File write is done')

    # problema 1 foloseste content
    print("2. Sum = ", compute_sum('prime_numbers_file'))

    # problema 3: numaratoare
    with open('probetext.txt', 'r', encoding='latin-1') as f:
        single, multiple = find_unique_words(f)
        print("3. Single: ", single[:10], ' ... first 10')
        print("3. Multiple: ", multiple[:10], ' ... first 10')

    # problem 4: merge sorted files
    file_names = ['sort/file1.txt', 'sort/file2.txt', 'sort/file3.txt']
    # it will crash because on dict comprehension I don't take in account empty files
    # file_names.append('sort/file4.txt')
    try:
        files_streams = [open(x, 'r') for x in file_names]
        result_stream = open('sort/result.txt', 'w')
        sort_files(files_streams, result_stream)
    except IOError:
        print('problems with the IO')
    finally:
        map(lambda x: x.close(), filter(lambda x: not x.closed, files_streams))
        print('4. Sorting done')

    # problem 5: crawl for href
    print(crawl_website_links("https://ep2015.europython.eu/en/"))
    print('5. in progress... nothing else to see here')
