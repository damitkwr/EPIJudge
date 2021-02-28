from test_framework import generic_test
from collections import Counter

def can_form_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    char_counter = Counter(s)
    foundOddPrevious = False
    if len(s) == 0:
        return True

    if len(s) % 2 == 0:
        for key, value in char_counter.items():
            if key != ' ':
                if value % 2 != 0:
                    return False
    else:
        for key, value in char_counter.items():
            if key != ' ':
                if value % 2 != 0:
                    if foundOddPrevious:
                        return False
                    else:
                        foundOddPrevious = True
    
    return True



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
