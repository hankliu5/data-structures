class DHeap:

    def __init__(self, isMaxHeap=False, d=2):
        if d < 1:
            raise BaseException('d should not be less than one')
        self.__isMaxHeap = isMaxHeap
        self.__d = d
        self.__list = []

    def size(self):
        return len(self.__list)

    def add(self, data):
        if data is None:
            raise TypeError('The type of data should not be NoneType')

        self.__list.append(data)
        self.__bubbleUp(self.size() - 1)

    def remove(self):
        if self.size == 0:
            raise IndexError('The list is empty')

        self.__swap(0, self.size() - 1)
        temp = self.__list.pop()
        self.__trickledown(0)
        return temp

    def get(self, index):
        if index < 0 or index > self.size() - 1:
            raise IndexError('index out of bound')

        return self.__list[index]

    def __bubbleUp(self, index):
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
        self.__list[index1], self.__list[
            index2] = self.__list[index2], self.__list[index1]
