import collections
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook

Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items: List[Item], capacity: int) -> int:
    # TODO - you fill in here.
    @functools.lru_cache(None)
    def find_max_val(item_index, cap):
        if item_index < 0:
            return 0

        without_item = find_max_val(item_index-1, cap)
        with_item = 0
        if not cap < items[item_index].weight:
            with_item = items[item_index].value + find_max_val(
                item_index-1, cap-items[item_index].weight)

        return max(without_item, with_item)

    return find_max_val(len(items)-1, capacity)


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('knapsack.py', 'knapsack.tsv',
                                       optimum_subject_to_capacity_wrapper))
