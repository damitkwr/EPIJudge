from typing import List

from test_framework import generic_test


def multiply(num1: List[int], num2: List[int]) -> List[int]:
    # TODO - you fill in here.
    if len(num1) >= len(num2):
        short_list, long_list = num2, num1
    else:
        short_list, long_list = num1, num2

    multiplyByAtEnd = 1

    if num1[0] < 0:
        num1[0] *= -1
        multiplyByAtEnd *= -1

    if num2[0] < 0:
        num2[0] *= -1
        multiplyByAtEnd *= -1

    results = [0] * ((len(short_list)) + (len(long_list)))
    offset = 0
    for n in reversed(short_list):
        carry = 0

        for i, m in enumerate(reversed(long_list)):
            tempNo = (n*m) + carry + results[(len(results)-1)-i-offset]
            results[(len(results)-1)-i-offset] = tempNo % 10
            carry = tempNo // 10

        if carry != 0:
            results[(len(results)-1)-len(long_list)-offset] = carry

        offset += 1 


    while results[0] == 0 and len(results) > 1:
        results.pop(0)

    results[0] *= multiplyByAtEnd

    if len(results) == 0:
        return [0]

    return results

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_multiply.py',
                                       'int_as_array_multiply.tsv', multiply))
