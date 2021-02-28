from typing import List

from test_framework import generic_test, test_utils
import collections

def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    # TODO - you fill in here.
    returnList = collections.defaultdict(list)

    for string in dictionary:
        stringKey = [0] * 26
        for c in string:
            if c is not ' ':
                stringKey[ord(c.lower())-ord('a')] += 1
            
        returnList[tuple(stringKey)].append(string)

    return [group for group in returnList.values() if len(group)>=2]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
