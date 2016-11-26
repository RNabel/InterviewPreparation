class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.val)


def create_basic_example():
    root = Node(12)
    left = Node(8)
    right = Node(15)
    root.left = left
    root.right = right

    return root


def create_complex_example():
    root = Node(10)
    left_par = Node(12)
    right_par = Node(15)

    left_child1 = Node(25)
    left_child2 = Node(30)

    right_child1 = Node(36)

    root.left = left_par
    root.right = right_par
    left_par.left = left_child1
    left_par.right = left_child2

    right_par.left = right_child1

    return root


left_most = None
last = None


def connect(root):
    """
    Recursively converts BST nodes to form Doubly-linked lists.
    :param root: The root to call
    :return: a tuple with the left most, current, and right-most element
    """
    global left_most, last
    if root is not None:
        connect(root.left)
        # print root

        # If left_most set current node as left_most
        if root.left is None and left_most is None:
            left_most = root

        else:
            # Connect to left sub-tree.
            root.left = last
            root.left.right = root
            last = root

        # check if right-hand leaf node, if so set `last` to current node.
        if root.right is None:
            last = root
            root.right = left_most
        else:
            connect(root.right)


if __name__ == '__main__':
    node = create_complex_example()
    connect(node)
    node = left_most

    seen_nodes = set()
    print node

    while node.right is not None and node not in seen_nodes:
        seen_nodes.add(node)
        node = node.right
        print node.val
    print "..."
