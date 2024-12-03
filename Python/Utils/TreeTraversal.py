def in_order_traversal(node):
    # in_order_traversal: Visits the left subtree, the root node, and then the right subtree.
    if node:
        in_order_traversal(node.left)
        print(node.value, end=' ')
        in_order_traversal(node.right)

def pre_order_traversal(node):
    # pre_order_traversal: Visits the root node, the left subtree, and then the right subtree.
    if node:
        print(node.value, end=' ')
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    # post_order_traversal: Visits the left subtree, the right subtree, and then the root node
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.value, end=' ')