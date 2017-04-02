class CLinkedList:
    """Circular doubly linked list.

    Attributes:
        __nelem: The number of elements
        __head: The first element of the list
    """

    def __init__(self):
        self.__nelem = 0
        self.__head = None

    def size(self):
        return self.__nelem

    def add(self, index, element):
        """Adds a new node with a element at specific position.

        Args:
            index: The index that we want to insert the node.
            element: The data for the new node.
        """
        if self.__index_check(index) and self.__data_check(element):
            if self.__nelem == 0:
                newNode = Node(element)
                self.__head = newNode
                newNode.setPrev(newNode)
                newNode.setNext(newNode)
            elif index == 0:
                newNode = Node(element)
                newNode.setNext(self.__head.getPrev().getNext())
                newNode.setPrev(self.__head.getPrev())
                self.__head.getPrev().setNext(newNode)
                self.__head.setPrev(newNode)
                self.__head = newNode
            else:
                cursor = self.__getNode(index)
                newNode = Node(element)
                newNode.setPrev(cursor.getPrev())
                newNode.setNext(cursor)
                cursor.getPrev().setNext(newNode)
                cursor.setPrev(newNode)
            self.__nelem += 1

    def get(self, index):
        """Returns the data of the specific node."""
        if self.__index_check(index):
            cursor = self.__getNode(index)
            return cursor.getElement()

    def set(self, index, data):
        """Sets a new data to the node and returns the previous data."""
        prevData = None
        if self.__index_check(index) and self.__data_check(data):
            cursor = self.__getNode(index)
            prevData = cursor.getElement()
            cursor.setElement(data)

        return prevData

    def remove(self, index):
        """Removes the specific node and returns its data."""
        prevData = None
        if self.__index_check(index):
            cursor = self.__getNode(index)
            prevData = cursor.getElement()
            if index == 0:
                self.__head = self.__head.getNext()
            cursor.remove()
        self.__nelem -= 1
        return prevData

    def clear(self):
        """Clears all nodes in the list."""
        for i in range(0, self.__nelem):
            self.remove(0)

    def isEmpty(self):
        """Returns the list is empty or not."""
        return self.__nelem == 0

    def __index_check(self, index):
        """Checks the index is valid or not.

        Raises:
            IndexError: if index is out of bound.
        """
        if index > self.__nelem or index < 0:
            raise IndexError('index is out of bound')
        else:
            return True

    def __data_check(self, data):
        """Checks the data is valid or not.

        Raises:
            TypeError: if the data is NoneType.
        """
        if data is None:
            raise TypeError
        else:
            return True

    def __getNode(self, index):
        """Returns the specific node."""
        cursor = self.__head
        for i in range(0, index):
            cursor = cursor.getNext()
        return cursor


class Node:
    """The Nodes containing the data, which are used in the linked list.

    Attributes:
        __data: The data we want to store.
        __next: The reference stores the next node.
        __prev: The reference stores the previous node.
    """
    def __init__(self, element):
        self.__data = element
        self.__next = None
        self.__prev = None

    def remove(self):
        self.__prev.setNext(self.__next)
        self.__next.setPrev(self.__prev)

    def setPrev(self, p):
        self.__prev = p

    def setNext(self, n):
        self.__next = n

    def setElement(self, data):
        self.__data = data

    def getNext(self):
        return self.__next

    def getPrev(self):
        return self.__prev

    def getElement(self):
        return self.__data
