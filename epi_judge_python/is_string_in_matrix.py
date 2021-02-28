from typing import List
import functools
from test_framework import generic_test


def is_pattern_contained_in_grid(grid: List[List[int]],
                                 pattern: List[int]) -> bool:
    # TODO - you fill in here.

    @functools.lru_cache(None)
    def is_pattern_contained_recurse(offset, x, y):
        if offset == len(pattern):
            return True

        if (not(0 <= x < len(grid) and 0 <= y < len(grid[x])) or grid[x][y] != pattern[offset]):
            return False

        return any(is_pattern_contained_recurse(offset+1, *new_xy) for new_xy in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)))

    return any(is_pattern_contained_recurse(0, search_x, search_y) for search_x in range(len(grid)) for search_y in range(len(grid[search_x])))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_in_matrix.py',
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
