from functools import partial, reduce, cache, lru_cache
from operator import add, mul

def test_pipe():
    add_one = partial(add, 1)
    double = partial(mul, 2)

    def pipe(*functions):
        return reduce(lambda f, g: lambda x: g(f(x)), functions)

    operations = [add_one, double, double]

    assert pipe(
        partial(map, pipe(*operations)),
        list,
    )([1,2,3,4]) == [8,12,16,20]


def test_cache():
    @cache
    def fib(n):
        return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

    print(fib(100))

    @lru_cache
    def fib(n):
        return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

    print(fib(100))

if __name__ == "__main__":
    test_pipe()

