import unittest
from lecture_tuesday import LinkNode, Queue


class LectureTuesdayTest(unittest.TestCase):
    def setUp(self):
        self.node = LinkNode(7)
        self.queue = Queue(self.node)

    def test_is_instance(self):
        self.assertTrue(isinstance(self.node, LinkNode))

    def test_has_correct_value(self):
        """It should have a value of 7
        """
        self.assertEqual(self.node.value, 7)

    def test_init_queue(self):
        self.assertTrue(isinstance(self.queue, Queue))

    def test_enqueue(self):
        self.queue.enqueue(10)
        self.assertEqual(self.queue.head.value, 10)

    def test_dequeue(self):
        self.assertEqual(self.queue.dequeue(), 7)
        self.assertEqual(self.queue.head, None)
        self.assertEqual(self.queue.tail, None)

        self.queue.enqueue(1)
        self.queue.enqueue(10)
        self.assertEqual(self.queue.head.value, 10)
        self.assertEqual(self.queue.dequeue(), 1)
        self.assertEqual(self.queue.tail.value, 10)

    def test_get_middle(self):
        # test one item
        self.assertEqual(self.queue.get_middle(), 7)
        # test empty
        self.queue.dequeue()
        self.assertEqual(self.queue.get_middle(), None)
        # test odd number
        self.queue.enqueue(3)
        self.queue.enqueue(10)
        self.queue.enqueue(5)
        self.queue.enqueue(7)
        self.queue.enqueue(9)
        self.assertEqual(self.queue.get_middle(), 5)

        # test even number
        self.queue.enqueue(9)
        self.assertEqual(self.queue.get_middle(), 5)


if __name__ == '__main__':
    unittest.main()
