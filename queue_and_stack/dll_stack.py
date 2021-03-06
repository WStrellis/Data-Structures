# from doubly_linked_list import DoublyLinkedList
import doubly_linked_list


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        self.storage = doubly_linked_list.DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_tail(value)
        self.size = len(self.storage)

    def pop(self):
        val = self.storage.remove_from_tail()
        self.size = len(self.storage)
        return val

    def len(self):
        return self.size
