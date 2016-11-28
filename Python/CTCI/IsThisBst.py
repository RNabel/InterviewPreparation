class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
last = -1


def check_binary_search_tree_(root):
    global last
    if root is None:
        return True

    if not check_binary_search_tree_(root.left):
        return False

    if not last < root.data:
        return False

    last = root.data
    return check_binary_search_tree_(root.right)

if __name__ == '__main__':
    root = Node(10)
    left = Node(6)
    right = Node(12)
    root.left = left
    root.right = right
    print check_binary_search_tree_(root)
