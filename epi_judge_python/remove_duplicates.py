import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class Name:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name, self.last_name = first_name, last_name

    def __eq__(self, o) -> bool:
        return self.first_name == o.first_name

    def __lt__(self, other) -> bool:
        return (self.first_name < other.first_name
                if self.first_name != other.first_name else
                self.last_name < other.last_name)

    def __repr__(self):
        return '%s %s' % (self.first_name, self.last_name)

def eliminate_duplicate(A: List[Name]) -> None:
    # TODO - you fill in here.
    A.sort()
    write_index = 1

    for i in range(1, len(A)):
        if A[i].first_name != A[write_index-1].first_name:
            A[write_index] = A[i]
            write_index += 1

    del A[write_index:]



@enable_executor_hook
def eliminate_duplicate_wrapper(executor, names):
    names = [Name(*x) for x in names]

    executor.run(functools.partial(eliminate_duplicate, names))

    return names


def comp(expected, result):
    return all([
        e == r.first_name for (e, r) in zip(sorted(expected), sorted(result))
    ])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('remove_duplicates.py',
                                       'remove_duplicates.tsv',
                                       eliminate_duplicate_wrapper, comp))
