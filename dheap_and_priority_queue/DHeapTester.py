import unittest
from DHeap import DHeap


class DHeapTester(unittest.TestCase):

    def setUp(self):
        self.BINARY_SIZE = 7
        self.TERNARY_SIZE = 13

    def testSizeAndAdd(self):
        heap = DHeap()
        self.assertEqual(heap.size(), 0)
        for i in range(0, self.BINARY_SIZE):
            heap.add(i)
            self.assertEqual(heap.size(), i + 1)
        for i in range(0, self.BINARY_SIZE):
            self.assertEqual(i, heap.get(i))

    def testAddNone(self):
        heap = DHeap()
        with self.assertRaises(TypeError):
            heap.add(None)

    def testBubbleUp1(self):
        maxHeap = DHeap(True)
        maxHeap.add(88)
        maxHeap.add(80)
        maxHeap.add(33)
        maxHeap.add(55)
        maxHeap.add(85)
        self.assertEqual(88, maxHeap.get(0))
        self.assertEqual(85, maxHeap.get(1))
        self.assertEqual(33, maxHeap.get(2))
        self.assertEqual(55, maxHeap.get(3))
        self.assertEqual(80, maxHeap.get(4))

    def testBubbleUp2(self):
        minHeap = DHeap()
        self.assertEqual(minHeap.size(), 0)
        for i in range(0, self.BINARY_SIZE):
            minHeap.add(i + 1)
            self.assertEqual(minHeap.size(), i + 1)
        for i in range(0, self.BINARY_SIZE):
            self.assertEqual(i + 1, minHeap.get(i))
        minHeap.add(0)
        self.assertEqual(0, minHeap.get(0))
        self.assertEqual(1, minHeap.get(1))
        self.assertEqual(3, minHeap.get(2))
        self.assertEqual(2, minHeap.get(3))
        self.assertEqual(5, minHeap.get(4))
        self.assertEqual(6, minHeap.get(5))
        self.assertEqual(7, minHeap.get(6))
        self.assertEqual(4, minHeap.get(7))

    def testBubbleUp3(self):
        minHeap = DHeap(False, 3)
        self.assertEqual(minHeap.size(), 0)
        for i in range(0, self.TERNARY_SIZE - 1):
            minHeap.add(i)
            self.assertEqual(minHeap.size(), i + 1)
        for i in range(0, self.TERNARY_SIZE - 1):
            self.assertEqual(i, minHeap.get(i))
        minHeap.add(-1)
        self.assertEqual(-1, minHeap.get(0))
        self.assertEqual(1, minHeap.get(1))
        self.assertEqual(2, minHeap.get(2))
        self.assertEqual(0, minHeap.get(3))
        self.assertEqual(4, minHeap.get(4))
        self.assertEqual(5, minHeap.get(5))
        self.assertEqual(6, minHeap.get(6))
        self.assertEqual(7, minHeap.get(7))
        self.assertEqual(8, minHeap.get(8))
        self.assertEqual(9, minHeap.get(9))
        self.assertEqual(10, minHeap.get(10))
        self.assertEqual(11, minHeap.get(11))
        self.assertEqual(3, minHeap.get(12))

    def testRemoveEmpty(self):
        heap = DHeap()
        with self.assertRaises(IndexError):
            heap.remove()

    def testRemove1(self):
        maxHeap = DHeap(True)
        maxHeap.add(88)
        maxHeap.add(80)
        maxHeap.add(33)
        maxHeap.add(55)
        maxHeap.add(85)
        self.assertEqual(88, maxHeap.remove())
        self.assertEqual(85, maxHeap.get(0))
        self.assertEqual(80, maxHeap.get(1))
        self.assertEqual(33, maxHeap.get(2))
        self.assertEqual(55, maxHeap.get(3))

    def testRemove2(self):
        maxHeap = DHeap(True)
        ls = [40, 18, 20, 15, 13, 9, 19, 1, 3, 8]
        for e in ls:
            maxHeap.add(e)

        # removes the root element(40) and checks the elements
        self.assertEqual(40, maxHeap.remove())
        self.assertEqual(20, maxHeap.get(0))
        self.assertEqual(18, maxHeap.get(1))
        self.assertEqual(19, maxHeap.get(2))
        self.assertEqual(15, maxHeap.get(3))
        self.assertEqual(13, maxHeap.get(4))
        self.assertEqual(9, maxHeap.get(5))
        self.assertEqual(8, maxHeap.get(6))
        self.assertEqual(1, maxHeap.get(7))
        self.assertEqual(3, maxHeap.get(8))

        # removes the root element(20) again and checks the elements
        self.assertEqual(20, maxHeap.remove())
        self.assertEqual(19, maxHeap.get(0))
        self.assertEqual(18, maxHeap.get(1))
        self.assertEqual(9, maxHeap.get(2))
        self.assertEqual(15, maxHeap.get(3))
        self.assertEqual(13, maxHeap.get(4))
        self.assertEqual(3, maxHeap.get(5))
        self.assertEqual(8, maxHeap.get(6))
        self.assertEqual(1, maxHeap.get(7))

    def testRemove3(self):
        minHeap = DHeap()
        for i in range(0, self.BINARY_SIZE):
            minHeap.add(i)
        self.assertEqual(0, minHeap.remove())
        self.assertEqual(1, minHeap.get(0))
        self.assertEqual(3, minHeap.get(1))
        self.assertEqual(2, minHeap.get(2))
        self.assertEqual(6, minHeap.get(3))
        self.assertEqual(4, minHeap.get(4))
        self.assertEqual(5, minHeap.get(5))

    def testRemove4(self):
        minHeap = DHeap()
        for i in range(0, self.BINARY_SIZE):
            minHeap.add(i)
        for i in range(0, self.BINARY_SIZE):
            self.assertEqual(i, minHeap.remove())

    def testRemove5(self):
        ternaryHeap = DHeap(False, 3)
        for i in range(0, self.BINARY_SIZE):
            ternaryHeap.add(i)
        self.assertEqual(0, ternaryHeap.remove())
        self.assertEqual(1, ternaryHeap.get(0))
        self.assertEqual(4, ternaryHeap.get(1))
        self.assertEqual(2, ternaryHeap.get(2))
        self.assertEqual(3, ternaryHeap.get(3))
        self.assertEqual(6, ternaryHeap.get(4))
        self.assertEqual(5, ternaryHeap.get(5))


if __name__ == '__main__':
    unittest.main()
