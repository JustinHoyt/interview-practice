from functools import partial, reduce, lru_cache, cache
from operator import add, mul, lt, pow, sub, abs, truediv
from statistics import mean
from itertools import repeat
from time import time, sleep

class Node:
    def __init__(self, key: int, val: int, left=None, right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right


double = partial(mul, 2)
add_one = partial(add, 1)
pipe = lambda *functions: reduce(lambda f, g: lambda x: g(f(x)), functions)


def timer(function):
    def wrapper(*args, **kwargs):
        before = time()
        function(*args, **kwargs)
        print(f"Function took {time() - before} seconds")

    return wrapper


def test_approx_sqrt():
    flip = lambda f: lambda *a: f(*reversed(a))
    div2 = lambda x: x / 2
    square = lambda x: x ** 2
    avg = lambda *args: mean(args)
    variance = .001

    tolerance = lambda x, y: pipe(
       square,
       partial(flip(sub), x),
       abs
    )(y)

    approx_ = lambda x, y: y if tolerance(x,y) < variance else pipe(
        partial(truediv, x),
        partial(avg, y),
        partial(approx_, x),
    )(y)

    approx = lambda x: pipe(
        div2,
        partial(approx_, x),
        partial(round, ndigits=2)
    )(x)

    assert approx(2) == 1.41
    assert approx(3) == 1.73


def test_pipe():
    operations = [add_one, double, double]

    assert pipe(
        partial(map, pipe(*operations)),
        list,
    )([1,2,3,4]) == [8,12,16,20]


    def getattrs(obj, *attrs):
        def _getattr(acc, prop):
            return getattr(acc, prop) if acc is not None else None
        return reduce(_getattr, attrs, obj)


    head = Node(1, 1)
    head.right = Node(2,2)
    head.right.right = Node(3,3)


    getattr(head, 'right')
    assert getattrs(head, 'right', 'right', 'val') == 3


def test_apply_n():
    def repeat(obj, n):
        return [obj for _ in range(n)]


    def apply_n_recursive(fn, n, x):
        return fn(x) if n == 1 else fn(apply_n_recursive(fn, n - 1, x))


    def apply_n(fn, n):
        return reduce(pipe, repeat(fn, n))


    def grow_one_year(yearly_savings, x):
        return x * 1.07 + yearly_savings


    def investment_return(investment, years, yearly_savings):
        return pipe(
            apply_n(partial(grow_one_year, yearly_savings), years),
            "${:,.2f}".format,
        )(investment)


    assert investment_return(10000, 40, 5000) == "$1,147,920.14"


def test_decorator():

    @timer
    def run():
        sleep(0.01)

    run()


def test_cache():
    @cache
    def fib(n):
        return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

    assert fib(100) == 573147844013817084101

    @lru_cache
    def fib(n):
        return 1 if n <= 1 else fib(n - 1) + fib(n - 2)

    assert fib(100) == 573147844013817084101


if __name__ == "__main__":
    test_pipe()
    test_cache()
    test_apply_n()
    test_decorator()

