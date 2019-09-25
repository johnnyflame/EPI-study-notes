import collections


def balanced_binary_tree(root):
    """
    9.1 Check if a binary tree is balanced

    :param root:
    :return:
    """

    BalancedStatusWithHeight = collections.namedtuple(
        'BalancedStatusWithHeight', ('balanced','height')
    )

    # First value of the return value indicates if tree is balanced, and if balanced,
    # the second value of teh return value is the height of the tree
    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True,-1)

        left_result = check_balanced(tree.left)

        if not left_result.balanced:
            return BalancedStatusWithHeight(False,0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            # Right subtree is not balanced
            return BalancedStatusWithHeight(False,0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1

        return BalancedStatusWithHeight(is_balanced, height)


    return check_balanced(root).balanced


def lca_with_parents(t1,t2):
    """

    9.4. This problem is basically following the same idea of linked list intersection

    :param t1:
    :param t2:
    :return:
    """
    def get_depth(node):
        depth = 0
        while node:
            depth+=1
            node = node.parent

        return depth

    # Get the depth of these two nodes by tracing back to the roots
    depth_0,depth_1 = get_depth(t1),get_depth(t2)
    # Make node_0 as teh deeper node in order to simplify the code

    if depth_1 > depth_0:
        t1,t2 = t2,t1

    # Ascends from the deeper root
    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        t1 = t1.parent
        depth_diff -= 1

    while t1 != t2:
        t1,t2 = t1.parent,t2.parent

    return t1

