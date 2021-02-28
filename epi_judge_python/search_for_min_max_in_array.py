import collections
from typing import List

from test_framework import generic_test
from test_framework.test_failure import PropertyName

MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A: List[int]) -> MinMax:
    # TODO - you fill in here.
    if len(A) == 1:
        return MinMax(A[0], A[0])

    if A[0] < A[1]:
        globalMin, globalMax = A[0], A[1]
    else:
        globalMin, globalMax = A[1], A[0]


    for i in range(2, len(A)-1, 2):
        globalMin = min(A[i], A[i+1]) if min(A[i], A[i+1]) < globalMin else globalMin
        globalMax = max(A[i], A[i+1]) if max(A[i], A[i+1]) > globalMax else globalMax

    if len(A) % 2 != 0:
        globalMin = A[len(A)-1] if A[len(A)-1] < globalMin else globalMin
        globalMax = A[len(A)-1] if A[len(A)-1] > globalMax else globalMax

    return MinMax(globalMin, globalMax)


def res_printer(prop, value):
    def fmt(x):
        return 'min: {}, max: {}'.format(x[0], x[1]) if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_for_min_max_in_array.py',
                                       'search_for_min_max_in_array.tsv',
                                       find_min_max,
                                       res_printer=res_printer))
