from threading import Thread, Lock, current_thread
from time import sleep, time
from queue import Queue


def worker(q, lock):
    while True:
        value = q.get()

        with lock:
            print(f'in {current_thread().name} got {value}')

        q.task_done()


class Solution:
    def __init__(self):
        self.lock = Lock()
        self.val = 0
        self.queue = Queue()

    def unsafe_increment(self, amount):
        local_copy = self.val
        local_copy += amount
        sleep(0.1)
        self.val = local_copy

    def safe_increment(self, amount):
        with self.lock:
            local_copy = self.val
            local_copy += amount
            sleep(0.1)
            self.val = local_copy


def test_thread_safe_increment():
    instance = Solution()
    t1 = Thread(target = instance.safe_increment, args=(1,))
    t2 = Thread(target = instance.safe_increment, args=(1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    assert instance.val == 2


def test_thread_unsafe_increment():
    instance = Solution()
    t1 = Thread(target=instance.unsafe_increment, args=(1,))
    t2 = Thread(target=instance.unsafe_increment, args=(1,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    assert instance.val == 1


def test_thread_safe_queue():
    instance = Solution()

    num_threads = 10

    for i in range(num_threads):
        t = Thread(name=f'Thread{i+1}', target=worker, args=(instance.queue, instance.lock))
        t.daemon = True
        t.start()

    for x in range(20):
        instance.queue.put(x)

    instance.queue.join()


if __name__ == "__main__":
    test_thread_safe_increment()

