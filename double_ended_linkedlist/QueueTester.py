import unittest
from Queue import Queue


class QueueTester(unittest.TestCase):

    def setUp(self):
        self.ls = Queue()

    def testIsEmpty(self):
        self.assertTrue(self.ls.isEmpty())

    def testAdd(self):
        for i in range(0, 5):
            self.ls.add(i)
            self.assertEqual(self.ls.size(), i + 1)

    def testRemove(self):
        for i in range(0, 5):
            self.ls.add(i)
        for i in range(0, 5):
            self.assertEqual(self.ls.remove(), i)

    def testRemoveEmpty(self):
        with self.assertRaises(BaseException):
            self.ls.remove()

    def testAddNone(self):
        with self.assertRaises(TypeError):
            self.ls.add(None)


if __name__ == '__main__':
    unittest.main()
