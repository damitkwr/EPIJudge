from typing import List
import random
from test_framework import generic_test


# The numbering starts from one, i.e., if A = [3, 1, -1, 2]
# find_kth_largest(1, A) returns 3, find_kth_largest(2, A) returns 2,
# find_kth_largest(3, A) returns 1, and find_kth_largest(4, A) returns -1.
def find_kth_largest(k: int, A: List[int]) -> int:
    # TODO - you fill in here.
    def do_pivot_and_search(searchArray, k):
        print(len(searchArray))
        pivot = random.randint(0, len(searchArray)-1)
        larger, smaller = [], []
        for no in searchArray:
            if no > searchArray[pivot]:
                larger.append(no)
            elif no < searchArray[pivot]:
                smaller.append(no)

        if len(larger) > k-1:
            return False, larger
        elif len(larger) < k-1:
            return False, smaller
        else:
            return True, [pivot]

    found = False
    returnArray = A
    biggest = k
    while not found:
        print(found)
        found, returnArray, biggest = do_pivot_and_search(returnArray, biggest)    
    return returnArray[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('kth_largest_in_array.py',
                                       'kth_largest_in_array.tsv',
                                       find_kth_largest))
