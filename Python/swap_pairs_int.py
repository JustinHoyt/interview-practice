import math

def pop(num: int) -> tuple[int, int]:
    digit = num % 10
    new_num = math.floor(num / 10)

    return new_num, digit


def get_length(num: int) -> int:
    if num == 0:
        return 0
    return math.floor(math.log10(num)) + 1


def push_left(num, digit) -> int:
    num_digits = get_length(num)

    return num + digit * 10 ** num_digits


def swap_pairs_int(num: int) -> int:
    result = 0
    while get_length(num) > 1:
        num, right_digit = pop(num)
        num, left_digit = pop(num)

        result = push_left(result, left_digit)
        result = push_left(result, right_digit)

    if get_length(num) == 1:
        _, digit = pop(num)
        result = push_left(result, digit)

    return result



def test_happy_path():
    assert swap_pairs_int(1234) == 2143

def test_odd_length():
    assert swap_pairs_int(123) == 132

if __name__ == "__main__":
    test_happy_path()
