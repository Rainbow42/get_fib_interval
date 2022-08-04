from typing import List


def get_fib_interval(n: int) -> List[int]:
    """
    :param n: Входное число, для которого требуется подсчитать последовательность фибоначчи и найти интервал
    :return: возвращает интервал
    """
    if n <= 0:
        raise

    el_fib_1, el_fib_2 = 0, 1
    # before_last
    before_last = 0  # сохранения промежуточного результата числа фибоначчи res -2
    last_res = 0  # сохранения предыдущего результата числа фибоначчи res - 1
    # так как для n не нужно вычислять конец последовательности фибоначчи,
    # но гарантировано приходится увеличивать n + 1, если n < 6
    # так как если n = 3, то краем интервала будет 2 и т.п.
    tmp = n
    res = 0

    if n < 6:
        n += 1

    for _ in range(n):
        res = el_fib_1 + el_fib_2

        if res > tmp:
            # первый же промежуточный результат будет концом интервала
            if last_res == tmp:
                return [before_last, res]
            return [last_res, res]
        before_last, last_res = last_res, res
        el_fib_1, el_fib_2 = el_fib_2, res
    return [last_res, res]


assert get_fib_interval(2) == [1, 3]
assert get_fib_interval(3) == [2, 5]
assert get_fib_interval(4) == [3, 5]
assert get_fib_interval(5) == [3, 8]
assert get_fib_interval(6) == [5, 8]
assert get_fib_interval(7) == [5, 8]
assert get_fib_interval(8) == [5, 13]
assert get_fib_interval(9) == [8, 13]
assert get_fib_interval(13) == [8, 21]
assert get_fib_interval(22) == [21, 34]
