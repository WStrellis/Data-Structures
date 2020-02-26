# import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack
import dll_queue
import dll_stack


class BinarySearchTree:
    _root = None

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if no root
        if not BinarySearchTree._root:
            # insert value as root
            BinarySearchTree._root = BinarySearchTree(value)
        # else
        # compare value to root
        if value >= self.value:
            # if larger and root-right child is null:
            if not self.right:
                # add as right child
                self.right = BinarySearchTree(value)
        # else move to right child and repeat
            else:
                self.right.insert(value)
        if value < self.value:
            # if smaller and root-left child is null:
            if not self.left:
                # add as left child
                self.left = BinarySearchTree(value)
        # else move to left child and repeat
            else:
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
