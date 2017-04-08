import unittest
from BSTree import BSTree
from BSTIterator import BSTIterator


class BSTreeTester(unittest.TestCase):

    def setUp(self):
        self.list = [20, 10, 30, 5, 15, 1, 2, 25, 40, 50]
        self.tree = BSTree()

    def testEmpty(self):
        self.assertTrue(self.tree.empty())
        self.insert()
        self.assertTrue(not self.tree.empty())

    def testHeight(self):
        self.assertEqual(self.tree.height(), -1)
        self.insert()
        self.assertEqual(self.tree.height(), 4)

    def testFindEmpty(self):
        self.assertTrue(self.tree.find(1) == BSTIterator(None))

    def testInsert(self):
        for e in self.list:
            iterator, result = self.tree.insert(e)
            self.assertEqual(iterator.curr.data, e)
            self.assertTrue(result)

    def testFindElement(self):
        self.insert()
        for e in self.list:
            self.assertEqual(self.tree.find(e).curr.data, e)
        self.assertEqual(self.tree.find(-1).curr, None)

    def testSize(self):
        self.insert()
        self.assertEqual(self.tree.size(), 10)

    def testSuccessor(self):
        self.insert()
        itr = self.tree.begin()
        for e in sorted(self.list):
            self.assertEqual(itr.curr.data, e)
            itr += 1
        # Tests the end of the iterator points to the None
        self.assertTrue(itr == BSTIterator(None))

    def insert(self):
        for e in self.list:
            self.tree.insert(e)


if __name__ == '__main__':
    unittest.main()
