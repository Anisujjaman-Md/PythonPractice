from Quee import Queue


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            nodes = Queue()
            nodes.enqueue(self.root)

            while True:
                checking_node = nodes.dequeue()
                if checking_node.left is None:
                    checking_node.left = TreeNode(val)
                elif checking_node.right is None:
                    checking_node.right = TreeNode(val)
                else:
                    nodes.enqueue(checking_node.left)
                    nodes.enqueue(checking_node.right)


class BST():
    def __init__(self):
        self.root = None

    def __insert_value(self, node, value):
        if node is None:
            return

        if node.val == value:
            return
        elif value < node.val:
            if node.left is None:
                node.left = TreeNode(value)
            self.__insert_value(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            self.__insert_value(node.right, value)

    def insert(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self.__insert_value(self.root, val)

    def __in_order(self, node):
        if node is None:
            return
        self.__in_order(node.left)
        print(node.val, end=" ")
        self.__insert_value(node.right)

    def in_order(self):
        self.__insert_value(self.root)


bst = BST()

for i in [8, 9, 10, 44, 5, 200, 556, 12, 154]:
    bst.insert(i)
    print(bst)