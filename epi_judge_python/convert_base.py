from test_framework import generic_test
import string

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    # TODO - you fill in here.
    letterDict = dict(zip(list(range(10, 36)), string.ascii_uppercase))
    letterDict.update({0: '0', 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9'})
    numberDict = {v: k for k, v in letterDict.items()}
    if num_as_string[0] == '-':
        sign = "-"
        num_as_string  = num_as_string[1:]
    else:
        sign = ''
    multiplyBy = 1
    carry = 0
    returnList = []

    for c in reversed(num_as_string):
        carry += multiplyBy * (numberDict[c])
        multiplyBy *= b1

    while True:
        returnList.append(letterDict[carry % b2])
        carry //= b2
        if carry == 0:
            break
    returnList.append(sign)
    
    return "".join(reversed(returnList))


if __name__ == '__main__':
    # print((306)//13)
    # print(23//13)
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
