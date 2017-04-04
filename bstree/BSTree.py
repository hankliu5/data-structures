class BSTree:
    """Binary Search Tree

    Attributes:
        __nelems: the amount of elements in the tree.
        __root1: the reference of the root of the first tree.
        __root2: the reference of the root of the second tree.
    """

    def __init__(self):
        self.__nelems = 0
        self.__root1 = None
        self.__root2 = None

    def getRoot(self, treeChoice):
        """Returns the root node of certain tree based on the choice

        Raises:
            BaseException: when the choice is not either 1 or 2
        """
        if treeChoice == 1:
            return self.__root1
        elif treeChoice == 2:
            return self.__root2
        else:
            raise BaseException('please use integer 1 or 2')

    def getSize(self):
        """Returns the size of the tree."""
        return self.__nelems

    def insert(self, firstData, secondData):
        """Inserts paired elements into trees.

        Raises:
            TypeError: if the input data is NoneType.
        """
        if firstData is None or secondData is None:
            raise TypeError('The input data is None')

        newNode1 = BSTNode(firstData)
        newNode2 = BSTNode(secondData)
        newNode1.setOuter(newNode2)
        newNode2.setOuter(newNode1)

        if (self.__nelems == 0):
            self.__root1 = newNode1
            self.__root2 = newNode2
        else:
            self.__insertHelper(self.__root1, newNode1)
            self.__insertHelper(self.__root2, newNode2)

        self.__nelems += 1

    def findElem(self, elem):
        """Finds the specific element in the trees.

        Returns:
            A boolean value that indicates the element is in the trees or not

        Raises:
            TypeError: if elem is NoneType
        """
        if elem is None:
            raise TypeError

        return self.__findHelper(elem, self.__root1) is not None\
            or self.__findHelper(elem, self.__root2) is not None

    def findMoreInfo(self, elem):
        """Returns the data of the outer node of the specific node.

        Finds out the specific node in trees first then returns its outer
        node's data.

        Returns:
            Its outer node's data.

        Raises:
            TypeError: if elem is NoneType
            BaseException: if elem is not found in both trees.
        """

        if elem is None:
            raise TypeError

        node = self.__findHelper(elem, self.__root1)
        if node is not None:
            return node.getOuter().getData()

        node = self.__findHelper(elem, self.__root2)
        if node is not None:
            return node.getOuter().getData()

        raise BaseException('Element not found in both trees')

    def printTree(self, treeChoice):
        """Prints the elements in-order.

        Traverses the tree in-order and prints out the element based on the
        treeChoice.

        Raises:
            BaseException: when the treeChoice is not either 1 or 2
            IndexError: when the trees are empty.
        """
        if self.__nelems == 0:
            raise IndexError('empty tree')
        if treeChoice != 1 and treeChoice != 2:
            raise BaseException('wrong treeChoice')

        root = self.__root1 if treeChoice == 1 else self.__root2
        self.__printHelper(root)

    def __printHelper(self, root):
        """Helps to traverse the tree in-order and prints the results"""
        if root is None:
            return

        self.__printHelper(root.getLChild())
        print(repr(root.getData()) + " " + repr(root.getOuter().getData()))
        self.__printHelper(root.getRChild())

    def __findHelper(self, elem, root):
        """Helps to find out the specific item in the tree.

        Returns: if found, returns the node, else returns None
        """
        if root is None:
            return None

        if root.getData() == elem:
            return root

        elif root.getData() > elem:
            return self.__findHelper(elem, root.getLChild())

        else:
            return self.__findHelper(elem, root.getRChild())

    def __insertHelper(self, root, node):
        """Helps to find out the correct position to insert."""
        if node.getData() < root.getData():
            if root.getLChild() is None:
                root.setLChild(node)
            else:
                self.__insertHelper(root.getLChild(), node)
        else:
            if root.getRChild() is None:
                root.setRChild(node)
            else:
                self.__insertHelper(root.getRChild(), node)


class BSTNode:
    """Node class for BSTree.

    Attributes:
        __data: the data contained by each node
        __lChild: the reference points to the left child node.
        __rChild: the reference points to the right child node.
        __outer: the reference points to the corresponding node in the other
            tree.
    """

    def __init__(self, data, lChild=None, rChild=None, outer=None):
        self.__data = data
        self.__lChild = lChild
        self.__rChild = rChild
        self.__outer = outer

    def getData(self):
        return self.__data

    def getLChild(self):
        return self.__lChild

    def getRChild(self):
        return self.__rChild

    def getOuter(self):
        return self.__outer

    def setData(self, data):
        self.__data = data

    def setLChild(self, lChild):
        self.__lChild = lChild

    def setRChild(self, rChild):
        self.__rChild = rChild

    def setOuter(self, outer):
        self.__outer = outer
