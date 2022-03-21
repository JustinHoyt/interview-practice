from time import process_time_ns

def timer(function):
    def wrapper(*args, **kwargs):
        before = process_time_ns()
        res = function(*args, **kwargs)
        print(f"Function took {process_time_ns() - before} ns")
        return res

    return wrapper

