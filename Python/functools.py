from functools import partial, reduce, cache, lru_cache
from operator import add, mul

class Node:
    def __init__(self, key: int, val: int, left=None, right=None):
        self.val = val
        self.key = key
        self.left = left
        self.right = right

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


    def getattrs(obj, *attrs):
        def _getattr(acc, prop):
            return getattr(acc, prop) if acc is not None else None
        return reduce(_getattr, attrs, obj)


    head = Node(1, 1)
    head.right = Node(2,2)
    head.right.right = Node(3,3)


    getattr(head, 'right')
    print(getattrs(head, 'right', 'right', 'val'))


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

