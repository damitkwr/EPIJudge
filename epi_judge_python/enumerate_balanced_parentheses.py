from typing import List

from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs: int) -> List[str]:
    # TODO - you fill in here.

    results = []

    def helper(leftNo, rightNo, partial):
        nonlocal results
        if leftNo == num_pairs and rightNo == num_pairs:
            results.append("".join(partial))
            return

        if leftNo < num_pairs and leftNo >= rightNo:
            helper(leftNo+1, rightNo, partial+['('])
        
        if rightNo < num_pairs and rightNo < leftNo:
            helper(leftNo, rightNo+1, partial+[')'])

    helper(0, 0, [])
    return results




if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('enumerate_balanced_parentheses.py',
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
