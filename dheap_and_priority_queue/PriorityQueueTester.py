import unittest
from PriorityQueue import PriorityQueue


class PriorityQueueTester(unittest.TestCase):

    def setUp(self):
        self.SIZE = 7
        self.pq = PriorityQueue()

    def testAddNone(self):
        with self.assertRaises(TypeError):
            self.pq.add(None)

    def testPollEmpty(self):
        self.assertEqual(self.pq.poll(), None)

    def testPoll(self):
        for i in range(0, self.SIZE):
            self.pq.add(i)
            self.assertEqual(i + 1, self.pq.size())
        for i in range(0, self.SIZE):
            self.assertEqual(i, self.pq.poll())

    def testMaxPQPoll(self):
        self.pq = PriorityQueue(True)
        for i in range(0, self.SIZE):
            self.pq.add(i)
            self.assertEqual(i + 1, self.pq.size())
        for i in range(self.SIZE - 1, -1, -1):
            self.assertEqual(i, self.pq.poll())


if __name__ == '__main__':
    unittest.main()
