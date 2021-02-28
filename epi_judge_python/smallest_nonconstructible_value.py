from typing import List

from test_framework import generic_test


def smallest_nonconstructible_value(A: List[int]) -> int:
    # TODO - you fill in here.
    A.sort()
    res = 1
    for i in range(len(A)):
        if A[i] <= res:
            res += A[i]
        else:
            break
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('smallest_nonconstructible_value.py',
                                       'smallest_nonconstructible_value.tsv',
                                       smallest_nonconstructible_value))
