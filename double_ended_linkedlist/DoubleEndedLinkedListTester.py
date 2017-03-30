import unittest
from DoubleEndedLinkedList import DoubleEndedLinkedList


class DoubleEndedLinkedListTester(unittest.TestCase):

    def setUp(self):
        self.ls = DoubleEndedLinkedList()

    def testIsEmpty(self):
        self.assertTrue(self.ls.isEmpty())

    def testAddLast(self):
        for i in range(0, 5):
            self.ls.addLast(i)
            self.assertEqual(self.ls.size(), i + 1)

    def testAddFirst(self):
        for i in range(0, 5):
            self.ls.addFirst(i)
            self.assertEqual(self.ls.size(), i + 1)

    def testRemoveFirst(self):
        for i in range(0, 5):
            self.ls.addLast(i)
        for i in range(0, 5):
            self.assertEqual(self.ls.removeFirst(), i)

    def testRemoveLast(self):
        for i in range(0, 5):
            self.ls.addFirst(i)
        for i in range(0, 5):
            self.assertEqual(self.ls.removeLast(), i)

    def testRemoveEmpty(self):
        with self.assertRaises(BaseException):
            self.ls.removeFirst()
        with self.assertRaises(BaseException):
            self.ls.removeLast()

    def testAddNone(self):
        with self.assertRaises(TypeError):
            self.ls.addLast(None)
        with self.assertRaises(TypeError):
            self.ls.addFirst(None)


if __name__ == '__main__':
    unittest.main()
