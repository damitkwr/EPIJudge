from typing import List

from test_framework import generic_test


def longest_subarray_with_distinct_entries(A: List[int]) -> int:
    # TODO - you fill in here.
    start = 0
    longestLength = 0
    entries = dict()
    for i, letter in enumerate(A):
        if letter in entries:
            duplicateIndex = entries[letter]
            if duplicateIndex >= start:
                longestLength = max(longestLength, i-start)
                start = entries[letter]+1

        entries[letter] = i


    return max(longestLength, len(A)-start)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'longest_subarray_with_distinct_values.py',
            'longest_subarray_with_distinct_values.tsv',
            longest_subarray_with_distinct_entries))
