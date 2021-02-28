from test_framework import generic_test
import string

def is_palindrome(s: str) -> bool:
    # TODO - you fill in here.
    alphabet = string.ascii_lowercase
    left_index, right_index = 0, 0
    isPalindromic = True

    for i in range(len(s)):
        if s[i].lower() in alphabet:
            left_index = i
            break
    
   
    for i in reversed(range(len(s))):
        if s[i].lower() in alphabet:
            right_index = i
            break

    if left_index == right_index:
        return isPalindromic

                
    while left_index < right_index:
        if s[left_index].lower() != s[right_index].lower():
            isPalindromic = False
            break


        for i in range(left_index+1, len(s)):
            if s[i].lower() in alphabet:
                left_index = i
                break
            
        for i in reversed(range(right_index)):
            if s[i].lower() in alphabet:
                right_index = i
                break

    return isPalindromic


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
