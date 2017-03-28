import unittest
from CLinkedList import CLinkedList


class CLinkedListTest(unittest.TestCase):

    def setUp(self):
        self.ls = CLinkedList()

    def testAddAtZerothIndex(self):
        for i in range(4, -1, -1):
            self.ls.add(0, i)
        for i in range(0, 5):
            self.assertEqual(self.ls.get(i), i)

    def testAddTheNextIndex(self):
        for i in range(0, 5):
            self.ls.add(i, i)
        for i in range(0, 5):
            self.assertEqual(self.ls.get(i), i)

    def testAddTheSecondIndex(self):
        self.ls.add(0, 0)
        self.ls.add(1, 4)
        self.ls.add(1, 3)
        self.ls.add(1, 2)
        self.ls.add(1, 1)
        for i in range(0, 5):
            self.assertEqual(self.ls.get(i), i)

    def testSet(self):
        self.ls = CLinkedList()
        for i in range(0, 5):
            self.ls.add(0, 0)
        for i in range(0, 5):
            self.ls.set(i, i)
        for i in range(0, 5):
            self.assertEqual(self.ls.get(i), i)

    def testAddOutOfBound(self):
        self.ls = CLinkedList()
        with self.assertRaises(IndexError):
            self.ls.add(2, 1)

    def testSetOutOfBound(self):
        self.ls = CLinkedList()
        with self.assertRaises(IndexError):
            self.ls.set(2, 1)

    def testAddNullInput(self):
        self.ls = CLinkedList()
        with self.assertRaises(TypeError):
            self.ls.add(0, None)

    def testSetNullInput(self):
        self.ls = CLinkedList()
        self.ls.add(0, 0)
        with self.assertRaises(TypeError):
            self.ls.set(0, None)

    def testIsEmpty(self):
        self.ls = CLinkedList()
        self.assertTrue(self.ls.isEmpty())
        self.ls.add(0, 0)
        self.assertTrue(not self.ls.isEmpty())

    def testRemoveAtZerothIndex(self):
        for i in range(0, 5):
            self.ls.add(i, i)
        for i in range(0, 5):
            self.assertEqual(self.ls.remove(0), i)

    def testRemoveAtTheLastIndex(self):
        for i in range(0, 5):
            self.ls.add(i, i)
        for i in range(4, -1, -1):
            self.assertEqual(self.ls.remove(i), i)

    def testRemoveAtMiddle(self):
        for i in range(0, 5):
            self.ls.add(i, i)
        self.assertEqual(self.ls.remove(2), 2)
        self.assertEqual(self.ls.remove(2), 3)
        self.assertEqual(self.ls.remove(2), 4)

    def testClear(self):
        for i in range(0, 5):
            self.ls.add(i, i)
        self.ls.clear()
        self.assertTrue(self.ls.isEmpty())


if __name__ == '__main__':
    unittest.main()
