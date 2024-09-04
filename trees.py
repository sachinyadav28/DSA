"""
Binary Tree Programs
"""
import queue


class Node:
    def __init__(self, data=None) -> None:
        self.data = data
        self.right = None
        self.left = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def build_tree(self, root=None):
        val = input("Enter the data : ")
        root = Node(val)
        if val == "-1":
            return None

        print(f"Enter data for left of {val}")
        root.left = self.build_tree(root.left)

        print(f"Enter data for right of {val}")
        root.right = self.build_tree(root.right)

        return root

    def level_order_traversal(self, root):
        print(" ************ ")
        if not root:
            return

        q = queue.Queue()
        q.put(root)

        while not q.empty():
            level_size = q.qsize()  # no of elements at current level
            while level_size > 0:
                temp = q.get()
                print(temp.data, end=" ")
                if temp.left:
                    q.put(temp.left)
                if temp.right:
                    q.put(temp.right)
                level_size -= 1
            print()  # Newline after each level

    def in_order_travel(self, root):
        # LNR (Left recur, Node print, Right recur)
        if root is None:
            return root
        self.in_order_travel(root.left)
        print(root.data, end=" ")   
        self.in_order_travel(root.right)

    def pre_order_travel(self, root):
        # NLR (Node print, Left recur, Right recur)
        if root is None:
            return root
        print(root.data, end=" ")
        self.pre_order_travel(root.left)
        self.pre_order_travel(root.right)

    def post_order_travel(self, root):
        # LRN (Left recur, Right recur, Node print)
        if root is None:
            return root
        self.post_order_travel(root.left)
        self.post_order_travel(root.right)
        print(root.data, end=" ")

# 1 3 7 -1 -1 11 -1 -1 5 17 -1 -1 -1


bt = BinaryTree()
bt.root = bt.build_tree()
bt.in_order_travel(bt.root)
