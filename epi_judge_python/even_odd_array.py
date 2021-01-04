import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def even_odd(A: List[int]) -> None:
    # TODO - you fill in here.
    p1 = 0
    p2 = len(A)-1
    
    while p1 < p2:
        if A[p1] % 2 != 0:
            while A[p2] % 2 != 0:
                if p2 <= p1:
                    break
                p2 -= 1
            
            A[p1], A[p2] = A[p2], A[p1]

        p1 += 1 
        


@enable_executor_hook
def even_odd_wrapper(executor, A):
    before = collections.Counter(A)

    executor.run(functools.partial(even_odd, A))

    in_odd = False
    for a in A:
        if a % 2 == 0:
            if in_odd:
                raise TestFailure('Even elements appear in odd part')
        else:
            in_odd = True
    after = collections.Counter(A)
    if before != after:
        raise TestFailure('Elements mismatch')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('even_odd_array.py',
                                       'even_odd_array.tsv', even_odd_wrapper))
