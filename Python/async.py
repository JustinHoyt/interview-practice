import asyncio
import time
from functools import wraps

i = 0
async def say_after(delay, what):
    global i
    await asyncio.sleep(delay)
    print(what)
    i += 1
    return i

def say_sync(delay, what):
    time.sleep(delay)
    print(what)

def awaitify(fn):
    @wraps(fn)
    async def async_fn(*args, **kwargs):
        return fn(*args, **kwargs)

    return async_fn


async def wrap_async_example():
    print(f"wrap async example started at {time.strftime('%X')}")

    # coro1 = asyncio.coroutine(lambda: say_sync(1, "hello"))
    say_async = awaitify(say_sync)
    assert asyncio.iscoroutinefunction(say_async)

    say_coroutine = say_async(1, "this should display second")
    assert asyncio.iscoroutine(say_coroutine)

    say_future = asyncio.create_task(say_coroutine)
    assert asyncio.isfuture(say_future)

    print('this should display first')

    await say_future

    print(f"wrap async example finished at {time.strftime('%X')}")


async def async_examples():
    print(f"async examples started at {time.strftime('%X')}")

    s3 = asyncio.create_task(say_after(1, 'three'))
    s1 = say_after(1, 'one')
    s2 = say_after(1, 'two')
    print(await s2)
    print(await asyncio.gather(s1,s3))

    print(f"async examples finished at {time.strftime('%X')}")


asyncio.run(wrap_async_example())
asyncio.run(async_examples())
