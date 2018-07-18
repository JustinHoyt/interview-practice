def nth_fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return nth_fib(n-1) + nth_fib(n-2)

print(nth_fib(35))

def dyn_nth_fib(n):
    mem = {}
    return recurse(n, mem)

def recurse(n, mem):
    if n in mem:
        return mem[n]
    elif n == 0 or n == 1:
        return 1
    else:
        to_return = recurse(n-1, mem) + recurse(n-2, mem)
    mem[n] = to_return
    return to_return

print(dyn_nth_fib(35))
