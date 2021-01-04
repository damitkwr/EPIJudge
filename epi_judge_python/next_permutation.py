from typing import List

from test_framework import generic_test


def next_permutation(perm: List[int]) -> List[int]:
    # TODO - you fill in here.

    # Check for empty array
    if len(perm) == 0:
        return []

    # Left swaps
    numberSwapped = False
    swappedIndex = 0
    for i in reversed(range(len(perm))):
        for j in reversed(range(i)):
            if perm[i] > perm[j]:
                perm[j], perm[i] = perm[i], perm[j]
                numberSwapped = True
                swappedIndex = j + 1
                break
        if numberSwapped:
            break
            
    # Right swaps
    if numberSwapped:
        # Check if the swapped number is at the end of the array
        if (swappedIndex+1) >= len(perm):
            return perm
        else:
            # Breaking initial state
            rightNumberSwapped = False
            while (swappedIndex+1) < len(perm) or rightNumberSwapped:
                for i in range(swappedIndex+1, len(perm)):
                    if perm[swappedIndex] > perm[i]:
                        perm[swappedIndex], perm[i] = perm[i], perm[swappedIndex]
                        rightNumberSwapped = True
                        swappedIndex = i
                        break
                
                if not rightNumberSwapped:
                    break                    

                rightNumberSwapped = False           

            return perm
    else:
        return []
                                

    


if __name__ == '__main__':
    # for i in range(1, 4):
    #     print(i)
    exit(
        generic_test.generic_test_main('next_permutation.py',
                                       'next_permutation.tsv',
                                       next_permutation))
