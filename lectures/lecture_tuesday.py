
class LinkNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self, node=None):
        self.head = node
        self.tail = node

    def enqueue(self, value):
        new_node = LinkNode(value, self.head)
        if self.tail == None:
            self.tail = self.head
        self.head = new_node

    def dequeue(self):
        # emtpy queue
        if not self.head:
            return None
        # or one item
        if self.head == self.tail:
            current = self.head
            self.head = self.tail = None
            return current.value

        current = self.head
        while current.next != self.tail:
            current = current.next
        old = self.tail
        self.tail = current
        self.tail.next = None
        return old.value

    def get_middle(self):
        # return value of middle element
        if not self.head and not self.tail:
            return None
        elif self.head == self.tail:
            return self.head.value
        else:
            mid = self.head
            last = self.head
            try:
                while last is not None:
                    mid = mid.next
                    last = last.next.next
            except:
                return mid.value
