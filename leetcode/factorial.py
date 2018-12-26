import functools
import sys
sys.setrecursionlimit(30000)

from timeit import default_timer as timer


def factorial_rec(n):
    if n == 0:
        return 1
    return n * factorial_rec(n - 1)


def factorial_esoteric(n):
    return functools.reduce(lambda x, y: x * y, [1] + list(range(1, n + 1)))


def factorial_iterative(n):
    total = 1
    for i in range(1, n + 1):
        total *= i
    return total


n = 20000

start = timer()
factorial_rec(n)
end = timer()
print("recursive:", end - start)

start = timer()
factorial_iterative(n)
end = timer()
print("iterative: ", end - start)

start = timer()
factorial_esoteric(n)
end = timer()
print("esoteric:", end - start)
