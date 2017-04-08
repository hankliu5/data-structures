class BSTNode():
    """Node class for binary search tree

    Attributes:
        __left: the left child of the node
        __right: the right child of the node
        __parent: the parent node of this node
        __data: the data contained by this node
    """

    def __init__(self, data):
        self.__left = None
        self.__right = None
        self.__parent = None
        self.__data = data

    # Getters and setters for the attributes
    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    def successor(self):
        """Finds and returns the next in-order successor node"""
        if self.__right is not None:
            curr = self.__right
            while curr.__left is not None:
                curr = curr.__left

        else:
            curr = self.__parent
            while curr is not None and curr.data < self.__data:
                curr = curr.__parent

        return curr
