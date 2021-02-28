from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


# def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
#     # TODO - you fill in here.
#     def is_balanced(node: BinaryTreeNode, low_range=float( '-inf'), high_range=float('inf')):
#         if not node:
#             return True
#         elif not low_range <= node.data <= high_range:
#             return False
#         else:
#             return (is_balanced(node.left, low_range=low_range, high_range=node.data)) and (is_balanced(node.right, low_range=node.data, high_range=high_range))

#     return is_balanced(tree)

def is_binary_tree_bst(tree: BinaryTreeNode) -> bool:
    min_value, max_value = float('-inf'), float('inf')
    node_stack = []
    node_stack.append((tree, min_value, max_value))

    if not tree:
        return True

    while node_stack:
        node, node_min, node_max = node_stack.pop()
        if not node_min <= node.data <= node_max:
            return False
        if node.right:
            node_stack.append((node.right, node.data, node_max))
        if node.left:
            node_stack.append((node.left, node_min, node.data))

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_tree_a_bst.py', 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))
