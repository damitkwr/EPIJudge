from test_framework import generic_test
import collections

def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # TODO - you fill in here.
    letterDict = dict()
    for c in magazine_text:
        if c != ' ':
            letterDict[c] = letterDict.get(c, 0) + 1

    for c in letter_text:
        if c != ' ':
            char_count = letterDict.get(c, 0)
            if char_count == 0:
                return False
            else:
                letterDict[c] = letterDict[c]-1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
