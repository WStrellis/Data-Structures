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
        # compare target to self.value
        if target == self.value:
            # if match return True
            return True
        # if less and  left child recursively call on left child
        elif self.left and target < self.value:
            return self.left.contains(target)
        # if larger and  right child recursively call on right child
        elif self.right and target > self.value:
            return self.right.contains(target)
        # else return false
        return False

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right:
            return self.right.get_max()
        return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    def for_each(self, cb):
        # call cb on self
        cb(self.value)
        # if self.right call for_each on right
        if self.right:
            self.right.for_each(cb)
        # if self.left call for_each on left
        if self.left:
            self.left.for_each(cb)

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
