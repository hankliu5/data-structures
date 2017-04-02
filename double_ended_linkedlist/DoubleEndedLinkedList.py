class DoubleEndedLinkedList:
    """The Linked List with head and tail

    Attributes:
        __nelems: the number of elements
        __head: the reference to the head of the list
        __tail: the reference to the tail of the list
    """

    def __init__(self):
        self.__nelems = 0
        self.__head = None
        self.__tail = None

    def isEmpty(self):
        """Returns the linked list is empty or not."""
        return self.__nelems == 0

    def size(self):
        """Returns the size of the linked list."""
        return self.__nelems

    def addFirst(self, element):
        """Adds an element at the beginning of the list.

        Args:
            element: the element added to the list.

        Raises:
            TypeError: If the element is None.
        """
        if element is None:
            raise TypeError('The input element is NoneType')

        newNode = Node(element)
        if self.__nelems == 0:
            self.__head = self.__tail = newNode

        else:
            newNode.setNext(self.__head)
            self.__head = newNode

        self.__nelems += 1

    def addLast(self, element):
        """Adds an element at the end of the list.

        Args:
            element: the element added to the list.

        Raises:
            TypeError: If the element is None.
        """
        if element is None:
            raise TypeError('The input element is NoneType')

        newNode = Node(element)
        if self.__nelems == 0:
            self.__head = self.__tail = newNode

        else:
            self.__tail.setNext(newNode)
            self.__tail = newNode

        self.__nelems += 1

    def removeFirst(self):
        """Removes an element at the beginning of the list.

        Returns:
            The data contained by the removed element.

        Raises:
            BaseException: If the element is empty.
        """
        if self.__nelems == 0:
            raise BaseException('Empty List')

        temp = self.__head
        if self.__nelems == 1:
            self.__head = self.__tail = None

        else:
            self.__head = temp.getNext()
            temp.setNext(None)

        self.__nelems -= 1

        return temp.getData()

    def removeLast(self):
        """Removes an element at the end of the list.

        Returns:
            The data contained by the removed element.

        Raises:
            BaseException: If the element is empty.
        """

        if self.__nelems == 0:
            raise BaseException('Empty List')

        temp = self.__tail

        if self.__nelems == 1:
            self.__head = self.__tail = None

        else:
            curr = self.__head
            while curr.getNext().getNext() is not None:
                curr = curr.getNext()

            curr.setNext(None)
            self.__tail = curr

        self.__nelems -= 1
        return temp.getData()


class Node:
    """The Nodes containing the data, which are used in the linked list.

    Attributes:
        __data: The data we want to store.
        __next: The reference stores the next node.
    """

    def __init__(self, element):
        self.__data = element
        self.__next = None

    def getNext(self):
        """Returns the next node"""
        return self.__next

    def setNext(self, nextNode):
        """Sets the next node"""
        self.__next = nextNode

    def getData(self):
        """Returns the data contained by this node object."""
        return self.__data
