from BSTNode import BSTNode
from BSTIterator import BSTIterator


class BSTree():
    """Binary Search Tree

    Attributes:
        __root: the root of the tree
        __size: the size of the tree
    """

    def __init__(self):
        self.__root = None
        self.__size = 0

    def insert(self, data) -> (BSTIterator, bool):
        """Inserts data into a tree.

        Returns:
            A tuple contains a BSTIterator object which refers to the inserted
            node, and a boolean value that indicates the insertion is whether
            successful or not.
        """

        # if there is no root
        if self.__root is None:
            self.__root = BSTNode(data)
            self.__size += 1
            return (BSTIterator(self.__root), True)

        curr = self.__root
        parent = self.__root

        while curr is not None:
            if data < curr.data:
                parent = curr
                curr = curr.left
            elif data > curr.data:
                parent = curr
                curr = curr.right
            else:
                return (BSTIterator(curr), False)

        newNode = BSTNode(data)
        newNode.parent = parent
        if data < parent.data:
            parent.left = newNode
        elif data > parent.data:
            parent.right = newNode
        self.__size += 1
        return (BSTIterator(newNode), True)

    def find(self, data):
        """Finds the specific node in the tree.

        Returns:
            A BSTIterator object which refers to the specific node. The object
            will refers to None if not found.
        """
        curr = self.__root
        while curr is not None:
            if curr.data > data:
                curr = curr.left
            elif curr.data < data:
                curr = curr.right
            else:
                return BSTIterator(curr)
        return BSTIterator(None)

    def size(self):
        """Returns the size of the tree."""
        return self.__size

    def height(self):
        """Returns the height of the tree."""
        return self.__heightHelper(self.__root) - 1

    def empty(self):
        """Returns whether the tree is empty or not."""
        return self.__size == 0

    def begin(self) -> (BSTIterator):
        """Returns a BSTIterator object that refers to the first element with
        in-order traverse."""
        if self.__root is None:
            return BSTIterator(None)

        curr = self.__root
        while curr.left is not None:
            curr = curr.left
        return BSTIterator(curr)

    def end(self) -> (BSTIterator):
        """Returns a BSTIterator object that refers to the end of the tree,
        which is None."""
        return BSTIterator(None)

    def __heightHelper(self, node) -> (int):
        """Helps to find out the height of tree recursively.

        Returns: the height of the subtree.
        """
        if node is None:
            return 0

        left = self.__heightHelper(node.left)
        right = self.__heightHelper(node.right)
        return 1 + max(left, right)
