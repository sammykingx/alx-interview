#!/usr/bin/python3


''' A module that returns the minimum Operations it takes to
    get to n characters.

    Available operations:
        copy
        paste
'''


def minOperations(n):
    '''
    returns the minimum operations to get n H's
    '''
    min_operations = 0

    if n <= 1:
        return min_operations

    for i in range(2, n + 1):
        while n % i == 0:
            min_operations += i
            n /= i

    return min_operations


if __name__ == '__main__':
    from random import randint
    from time import time

    n = 4
    print("Min # of operations to reach {} char: {}".
          format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".
          format(n, minOperations(n)))

    start_time = time()

    for i in range(10):
        n = randint(2, 100)
        print("Min # of operations to reach {} char: {}".
              format(n, minOperations(n)))

    print('==> Program completed in {:.3f}s'.format(time() - start_time))
