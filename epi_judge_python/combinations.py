from typing import List

from test_framework import generic_test, test_utils


def combinations(n: int, k: int) -> List[List[int]]:
    # TODO - you fill in here.
    def recurse_combinations(start_index, partial_sol):
        nonlocal results
        if len(partial_sol) == k:
            results.append(partial_sol.copy())
            return

        
        for i in range(start_index, len(input_array)):
            partial_sol.append(input_array[i])
            recurse_combinations(i+1, partial_sol)
            partial_sol.pop()

    input_array = list(range(1, n+1))
    results = []
    recurse_combinations(0, [])

    return results



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'combinations.py',
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
