from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    # TODO - you fill in here.
    A[-1] += 1

    carry = 0
    for i in reversed(range(len(A))):

        tempNo = A[i] + carry
        A[i] = tempNo % 10
        carry = tempNo // 10
    
    if carry != 0:
        A.insert(0, 1)


    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
