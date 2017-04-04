import unittest
from BSTree import BSTree


class BSTreeTester(unittest.TestCase):

    def setUp(self):
        self.myTree = BSTree()
        self.myTree.insert("Richard", "Tran")
        self.myTree.insert("Pooja", "Bhat")
        self.myTree.insert("Zach", "Meyer")
        self.myTree.insert("Marina", "Langlois")
        self.myTree.insert("Thiago", "Marback")
        self.myTree.insert("Siwei", "Xu")
        self.myTree.insert("Annie", "Xiao")
        self.myTree.insert("Don", "Vo")
        self.myTree.insert("Haoran", "Sun")
        self.emptyTree = BSTree()

    def testGetRoot(self):
        self.assertEqual(self.myTree.getRoot(1).getData(), 'Richard')
        self.assertEqual(self.myTree.getRoot(2).getData(), 'Tran')
        self.assertEqual(self.emptyTree.getRoot(1), None)
        self.assertEqual(self.emptyTree.getRoot(2), None)

        with self.assertRaises(BaseException):
            self.myTree.getRoot(3)

    def testGetSize(self):
        self.assertEqual(self.myTree.getSize(), 9)
        self.assertEqual(self.emptyTree.getSize(), 0)

    def testFindElem(self):
        self.assertTrue(self.myTree.findElem("Richard"))
        self.assertTrue(self.myTree.findElem("Tran"))
        self.assertTrue(self.myTree.findElem("Pooja"))
        self.assertTrue(self.myTree.findElem("Bhat"))
        self.assertTrue(self.myTree.findElem("Zach"))
        self.assertTrue(self.myTree.findElem("Meyer"))
        self.assertTrue(self.myTree.findElem("Marina"))
        self.assertTrue(self.myTree.findElem("Langlois"))
        self.assertTrue(self.myTree.findElem("Thiago"))
        self.assertTrue(self.myTree.findElem("Marback"))
        self.assertTrue(self.myTree.findElem("Siwei"))
        self.assertTrue(self.myTree.findElem("Xu"))
        self.assertTrue(self.myTree.findElem("Annie"))
        self.assertTrue(self.myTree.findElem("Xiao"))
        self.assertTrue(self.myTree.findElem("Don"))
        self.assertTrue(self.myTree.findElem("Vo"))
        self.assertTrue(self.myTree.findElem("Haoran"))
        self.assertTrue(self.myTree.findElem("Sun"))
        self.assertTrue(not self.myTree.findElem("Hank"))
        self.assertTrue(not self.myTree.findElem("Liu"))

        with self.assertRaises(TypeError):
            self.myTree.findElem(None)

    def testFindMoreInfo(self):
        self.assertEqual("Tran", self.myTree.findMoreInfo("Richard"))
        self.assertEqual("Richard", self.myTree.findMoreInfo("Tran"))
        self.assertEqual("Bhat", self.myTree.findMoreInfo("Pooja"))
        self.assertEqual("Pooja", self.myTree.findMoreInfo("Bhat"))
        self.assertEqual("Meyer", self.myTree.findMoreInfo("Zach"))
        self.assertEqual("Zach", self.myTree.findMoreInfo("Meyer"))
        self.assertEqual("Langlois", self.myTree.findMoreInfo("Marina"))
        self.assertEqual("Marina", self.myTree.findMoreInfo("Langlois"))
        self.assertEqual("Marback", self.myTree.findMoreInfo("Thiago"))
        self.assertEqual("Thiago", self.myTree.findMoreInfo("Marback"))
        self.assertEqual("Xu", self.myTree.findMoreInfo("Siwei"))
        self.assertEqual("Siwei", self.myTree.findMoreInfo("Xu"))
        self.assertEqual("Xiao", self.myTree.findMoreInfo("Annie"))
        self.assertEqual("Annie", self.myTree.findMoreInfo("Xiao"))
        self.assertEqual("Vo", self.myTree.findMoreInfo("Don"))
        self.assertEqual("Don", self.myTree.findMoreInfo("Vo"))
        self.assertEqual("Sun", self.myTree.findMoreInfo("Haoran"))
        self.assertEqual("Haoran", self.myTree.findMoreInfo("Sun"))

        with self.assertRaises(TypeError):
            self.myTree.findMoreInfo(None)

        with self.assertRaises(BaseException):
            self.myTree.findMoreInfo("Hank")

    def testPrint(self):
        print()
        self.myTree.printTree(1)
        self.myTree.printTree(2)

        with self.assertRaises(BaseException):
            self.myTree.printTree(3)

        with self.assertRaises(IndexError):
            self.emptyTree.printTree(1)


if __name__ == '__main__':
    unittest.main()
