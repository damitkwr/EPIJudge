from typing import Optional

from bst_node import BstNode
from test_framework import generic_test


def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:
    # TODO - you fill in here.
    if not tree:
        return None
    currentNode, candidate = tree, None
    while currentNode:
        if currentNode.data > k:
            currentNode, candidate = currentNode.left, currentNode
        else:
            currentNode = currentNode.right
    # def find_key(node: BstNode, val):
        # returnNode = None
        # if node.left and not returnNode:
        #     returnNode = find_key(node.left, val)

        # if node.data > val and not returnNode:
        #     return node

        # if node.right and not returnNode:
        #     returnNode = find_key(node.right, val)
        
        # return returnNode

    return candidate


def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'search_first_greater_value_in_bst.py',
            'search_first_greater_value_in_bst.tsv',
            find_first_greater_than_k_wrapper))
