class DHeap:
    """D-nary min/max heap

    Attributes:
        __d: indicates how many children for a parent.
        __isMaxHeap: indicates it's min or max heap.
        __list: the structure that stores the data.
    """

    def __init__(self, isMaxHeap=False, d=2):
        """Initializes the heap object, with default binary minheap.

        Raises:
            BaseException: when d is less than 1.
        """
        if d < 1:
            raise BaseException('d should not be less than one')
        self.__isMaxHeap = isMaxHeap
        self.__d = d
        self.__list = []

    def size(self):
        """Returns the size of the heap."""
        return len(self.__list)

    def add(self, data):
        """Adds a new element into the heap.

        Raises:
            TypeError: if the data is NoneType.
        """
        if data is None:
            raise TypeError('The type of data should not be NoneType')

        self.__list.append(data)
        self.__bubbleUp(self.size() - 1)

    def remove(self):
        """Pops and returns the top element in the heap.

        Returns:
            The top element in the heap.

        Raises:
            IndexError: when the heap is empty.
        """
        if self.size == 0:
            raise IndexError('The heap is empty')

        self.__swap(0, self.size() - 1)
        temp = self.__list.pop()
        self.__trickledown(0)
        return temp

    def get(self, index):
        """Returns the specific index of element.

        Raises:
            IndexError: when input index is out of bound.
        """
        if index < 0 or index > self.size() - 1:
            raise IndexError('index out of bound')

        return self.__list[index]

    def __bubbleUp(self, index):
        """Helps to move the new element to the correct place."""
        if index == 0:
            return
        else:
            parentIndex = (index - 1) // self.__d
            data = self.__list[index]
            parentData = self.__list[parentIndex]
            if (data < parentData) and not self.__isMaxHeap:
                self.__swap(index, parentIndex)
                self.__bubbleUp(parentIndex)
            elif (parentData < data) and self.__isMaxHeap:
                self.__swap(index, parentIndex)
                self.__bubbleUp(parentIndex)

    def __trickledown(self, index):
        """Helps to move the element to the correct place after removing."""
        childIndex = self.__d * index + 1
        # checks whether the children are the leaves or not
        if (childIndex + 1 > self.size()):
            return

        # compares which child we're going to swap
        for i in range(2, self.__d + 1):
            currentIndex = self.__d * index + i
            if currentIndex > self.size() - 1:
                break
            else:
                curr = self.__list[currentIndex]
                child = self.__list[childIndex]
                if self.__isMaxHeap and (curr > child):
                    childIndex = currentIndex
                elif not self.__isMaxHeap and (curr < child):
                    childIndex = currentIndex

        # trickles down
        data = self.__list[index]
        childData = self.__list[childIndex]
        if data < childData and self.__isMaxHeap:
            self.__swap(index, childIndex)
            self.__trickledown(childIndex)
        elif data > childData and not self.__isMaxHeap:
            self.__swap(index, childIndex)
            self.__trickledown(childIndex)

    def __swap(self, index1, index2):
        """Helps to swap two elements."""
        self.__list[index1], self.__list[index2] \
            = self.__list[index2], self.__list[index1]
