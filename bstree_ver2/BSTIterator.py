from BSTNode import BSTNode


class BSTIterator:
    """The iterator for binary search tree.

    Attribute:
        __curr: the reference to the node in the tree.
    """

    def __init__(self, curr: BSTNode):
        self.__curr = curr

    def __eq__(self, other):
        return self.__curr == other.__curr

    def __ne__(self, other):
        return self.__curr != other.__curr

    def __add__(self, step):
        """Call the successor function and returns a new iterator contain the
        new reference"""
        for i in range(0, step):
            self.__curr = self.__curr.successor()
        return BSTIterator(self.__curr)

    @property
    def curr(self):
        """Getter for __curr"""
        return self.__curr
